# import pyaudio
# import wave
# import os
# import subprocess
# import servo

# # Configuración de la grabación de audio
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "grabacion.wav"



# # Inicialización de PyAudio
# audio = pyaudio.PyAudio()

# # Apertura del stream de audio
# stream = audio.open(format=FORMAT, channels=CHANNELS,
#                     rate=RATE, input=True,
#                     frames_per_buffer=CHUNK)

# # llevar servo a 90
# servo.move_to(s,90)

# print("Grabando...")

# # Lectura de los datos de audio
# frames = []
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("Terminado la grabación.")

# # Detención de la grabación
# stream.stop_stream()
# stream.close()
# audio.terminate()

# # Escritura del archivo de audio en formato WAV
# waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# waveFile.setnchannels(CHANNELS)
# waveFile.setsampwidth(audio.get_sample_size(FORMAT))
# waveFile.setframerate(RATE)
# waveFile.writeframes(b''.join(frames))
# waveFile.close()

# # Convertir el archivo WAV en formato MP3 usando ffmpeg
# subprocess.call(['ffmpeg', '-y', '-i', WAVE_OUTPUT_FILENAME, 'file.mp3'])

# # Eliminar el archivo WAV
# os.remove(WAVE_OUTPUT_FILENAME)

# print("El archivo de audio ha sido guardado en formato MP3.")

import config
import openai
import servo

def enviar_pregunta():

  openai.api_key = config.api_key

  f=open("file.mp3",'rb')
  transcript=openai.Audio.translate("whisper-1",f)
  print(transcript)

  question=transcript

  completion=openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"Answer in json format answer: yes/no/I don't know, level_of_confidence: from 0 to 100 and a short_answer: in <100 characters to the following question:{question}"}])
  print(completion.choices[0].message.content)

  # decodificar completion.choices[0].message.content (json) y extraer campo answer
  completion=completion.choices[0].message.content
  completion=completion[completion.find("answer")+9:completion.find("level_of_confidence")-3]
  print(completion)

  return completion,question

