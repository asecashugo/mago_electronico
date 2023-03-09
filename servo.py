

import RPi.GPIO as GPIO
import time

class Servo():
  def __init__(self,pin) -> None:
    self.PIN = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN, GPIO.OUT)
    print('servo initialized in pin '+str(self.PIN))
    self.p = GPIO.PWM(self.PIN, 50)
    self.duty_cycle=2.5
    self.p.start(self.duty_cycle) 
    self.speed=0.08
  def move_to(self,target_angle_deg):
    # translate angle_deg to duty cycle
    # 0 degrees = 2.5
    # 90 degrees = 5
    # 180 degrees = 12.5
    target_duty_cycle=2.5+target_angle_deg/180*10
    while abs(self.duty_cycle - target_duty_cycle)>2*self.speed:
      if self.duty_cycle < target_duty_cycle:
        self.duty_cycle+=self.speed
        self.p.ChangeDutyCycle(self.duty_cycle)
      else:
        self.duty_cycle-=self.speed
        self.p.ChangeDutyCycle(self.duty_cycle)
      # print('going to '+str(target_angle_deg)+' degrees, duty cycle: '+str(target_duty_cycle))
      time.sleep(0.01)
    # self.p.ChangeDutyCycle(target_duty_cycle)
    time.sleep(1)


def def_servo():

  servoPIN = 18
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)
  print('servo initialized in pin '+str(servoPIN))

  p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
  p.start(2.5) 
  return p

# lim_min=3
# lim_max=12
# step=0.01
# speed=40

# while True:
#   try:
#     for x in range(int(lim_min/step), int(lim_max/step), 1):
#       p.ChangeDutyCycle(x*step)
#       print(x*step)
#       time.sleep(1/speed)
#     for x in range(int(lim_max/step), int(lim_min/step), -1):
#       p.ChangeDutyCycle(x*step)
#       print(x*step)
#       time.sleep(1/speed)

#   except KeyboardInterrupt:
#     p.stop()
#     GPIO.cleanup()
#     break

def move_to(servo,angle_deg):
  # translate angle_deg to duty cycle
  # 0 degrees = 2.5
  # 90 degrees = 5
  # 180 degrees = 7.5
  # 270 degrees = 10
  # 360 degrees = 12.5
  duty_cycle=2.5+angle_deg/180*5

  servo.ChangeDutyCycle(duty_cycle)
  print('going to '+str(angle_deg)+' degrees, duty cycle: '+str(duty_cycle))
  time.sleep(1)
  # servo.stop()
  # GPIO.cleanup()