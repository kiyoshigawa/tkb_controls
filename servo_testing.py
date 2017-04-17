'''
This is a file for testing adafruit's python libraries and writing functions to control the tkb's Hi-Tec HS-322HD servos.
Author: kiyoshigawa
'''

from __future__ import division
import time

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

