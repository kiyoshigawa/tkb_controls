'''
This is a file for testing adafruit's python libraries and writing functions to control the tkb's Hi-Tec HS-322HD servos.
Author: kiyoshigawa
'''

from __future__ import division
import time
import servo

l0 = (
  servo.servo(controller=0x40, channel=0, servo_constant=0.106, theta=0, theta_min=-90, theta_max=90, pulse_mid=2200),
  servo.servo(controller=0x40, channel=1, servo_constant=0.106, theta=1, theta_min=-90, theta_max=90, pulse_mid=2200),
  servo.servo(controller=0x40, channel=2, servo_constant=0.106, theta=2, theta_min=-90, theta_max=90, pulse_mid=2200),
  servo.servo(controller=0x40, channel=3, servo_constant=0.106, theta=3, theta_min=-90, theta_max=90, pulse_mid=2200),
  servo.servo(controller=0x40, channel=4, servo_constant=0.106, theta=4, theta_min=-90, theta_max=90, pulse_mid=2200)
)

l0[4].initialize()
l0[4].initialize()

for s in l0:
  print(s.theta)

'''
OLD CODE FOR DIRECT CONTROL:

# Import the PCA9685 module.
import Adafruit_PCA9685

#default address of 40
pwm = Adafruit_PCA9685.PCA9685(0x40)

pwm.set_pwm_freq(400)

servo_low = 906
servo_mid = 2800
servo_high = 4014

pwm.set_pwm(0, 0, servo_mid)
pwm.set_pwm(1, 0, servo_mid)
pwm.set_pwm(2, 0, servo_mid)
pwm.set_pwm(3, 0, servo_mid)
pwm.set_pwm(4, 0, servo_mid)
'''
