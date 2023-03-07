import pyaudio
import wave
import os
import subprocess
import RPi.GPIO as GPIO
import time

import pregunta
import servo
import pantalla

# Configuración de la grabación de audio
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "file.wav"

# Configuración del botón y el LED
BUTTON_PIN = 5
LED_PIN = 6

# Inicialización de PyAudio
audio = pyaudio.PyAudio()

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

# Función para encender o apagar el LED
def set_led(state):
    GPIO.output(LED_PIN, state)

# Función para grabar audio
def grabar_audio():
    # Apertura del stream de audio
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Grabando...")

    # Lectura de los datos de audio mientras el botón esté presionado
    frames = []
    while GPIO.input(BUTTON_PIN) == GPIO.LOW:
        set_led(True)
        data = stream.read(CHUNK)
        frames.append(data)

    print("Terminado la grabación.")

    # Detención de la grabación
    set_led(False)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Escritura del archivo de audio en formato WAV
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    # Convertir el archivo WAV en formato MP3 usando ffmpeg
    subprocess.call(['ffmpeg', '-y', '-i', WAVE_OUTPUT_FILENAME, 'file.mp3'])

    # Eliminar el archivo WAV
    os.remove(WAVE_OUTPUT_FILENAME)

    print("El archivo de audio ha sido guardado en formato MP3.")

    completion,question= pregunta.enviar_pregunta()
    print('completion: ',completion)

    # tranform completion to lowercase
    completion=completion.lower()

    # if completion string contains 'yes' substring
    if 'yes' in completion:
        angulo=180
    elif 'no' in completion:
        angulo=0
    else:
        angulo=90
    
    return angulo,completion,question


pantalla= pantalla.Pantalla()

# Configuración de la interrupción del botón
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=grabar_audio, bouncetime=300)

# definir servo
s=servo.Servo(18)

# Ciclo principal del programa
while True:
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        time.sleep(0.1) # debounce
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            angulo,completion,question=grabar_audio()
            print('angulo: ',angulo)
            pantalla.show(completion)
            s.move_to(angulo)
        else:
            set_led(False)
    else:
        set_led(False)
        print('esperando...',end='\r')
        pantalla.show("esperando...")
        time.sleep(0.1) # debounce
