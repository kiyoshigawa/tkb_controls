'''
This is a file for testing adafruit's python libraries and writing functions to control the tkb's Hi-Tec HS-322HD servos.
Author: kiyoshigawa
'''


from __future__ import division
import time
import servo

#a simple debug print function
DEBUG = True

def log(s):
  if DEBUG:
    print(s)

l0 = (
  servo.servo(controller=0x40, channel=0, servo_constant=0.106, theta=0, default_pulse=2800, theta_min=-90, theta_max=90),
  servo.servo(controller=0x40, channel=1, servo_constant=0.106, theta=1, default_pulse=2801, theta_min=-90, theta_max=90),
  servo.servo(controller=0x40, channel=2, servo_constant=0.106, theta=2, default_pulse=2602, theta_min=-90, theta_max=90),
  servo.servo(controller=0x40, channel=3, servo_constant=0.106, theta=3, default_pulse=2803, theta_min=-90, theta_max=90),
  servo.servo(controller=0x40, channel=4, servo_constant=0.106, theta=4, default_pulse=2704, theta_min=-90, theta_max=90)
)

l0[4].initialize()

l0[3].theta = 20;

for s in l0:
  log(s.theta)

'''
#OLD CODE FOR DIRECT CONTROL:

# Import the PCA9685 module.
import Adafruit_PCA9685

#default address of 40
pwm = Adafruit_PCA9685.PCA9685(0x40)

pwm.set_pwm_freq(400)

servo_low = 906
servo_mid = 2800
servo_high = 4014

#usually good to leave on at 0 so the pulse will start at the beginning of every frequency cycle, and drop at the off value, which is a number between 0 and 4095
pwm.set_pwm(channel=0, on=0, off=servo_mid)
pwm.set_pwm(channel=1, on=0, off=servo_mid)
pwm.set_pwm(channel=2, on=0, off=servo_mid)
pwm.set_pwm(channel=3, on=0, off=servo_mid)
pwm.set_pwm(channel=4, on=0, off=servo_mid)
'''
