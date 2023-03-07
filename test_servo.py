import RPi.GPIO as GPIO
import time
import servo

p=servo.Servo(18)

try:
  while True:
    p.move_to(0)
    time.sleep(0.5)
    p.move_to(90)
    time.sleep(0.5)
    p.move_to(180)
    time.sleep(0.5)
    
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()