# This is a file for testing adafruit's python libraries and writing functions to control the tkb's Hi-Tec HS-322HD servos.
# Author: kiyoshigawa

import time
import servo

# A simple debug print function
DEBUG = True


def log(s):
    if DEBUG:
        print(s)

leg0 = (
    servo.servo(controller=0x40, channel=0, servo_constant=0.106, theta=0, default_pulse=1500, theta_min=-90, theta_max=90),
    servo.servo(controller=0x40, channel=1, servo_constant=0.106, theta=0, default_pulse=1500, theta_min=-90, theta_max=90),
    servo.servo(controller=0x40, channel=2, servo_constant=0.106, theta=0, default_pulse=1500, theta_min=-90, theta_max=90),
    servo.servo(controller=0x40, channel=3, servo_constant=0.106, theta=0, default_pulse=1500, theta_min=-90, theta_max=90),
    servo.servo(controller=0x40, channel=4, servo_constant=0.106, theta=0, default_pulse=1500, theta_min=-90, theta_max=90)
)

leg0[0].initialize()
time.sleep(1)
leg0[0].theta = 90
leg0[0].update()

time.sleep(1)
leg0[0].theta = -90
leg0[0].update()

time.sleep(1)
leg0[0].set_us_pulse(1500)
leg0[0].update()

time.sleep(1)
leg0[0].disable_all()
leg0[0].update()

# '''
# #OLD CODE FOR DIRECT CONTROL:

# # Import the PCA9685 module.
# import Adafruit_PCA9685

# #default address of 40
# pwm = Adafruit_PCA9685.PCA9685(0x40)
# log(pwm)
# pwm.set_pwm_freq(400)

# servo_low = 906
# servo_mid = 2800
# servo_high = 4014

# #usually good to leave on at 0 so the pulse will start at the beginning of every frequency cycle, and drop at the off value, which is a number between 0 and 4095
# pwm.set_pwm(channel=0, on=0, off=servo_mid)
# pwm.set_pwm(channel=1, on=0, off=servo_mid)
# pwm.set_pwm(channel=2, on=0, off=servo_mid)
# pwm.set_pwm(channel=3, on=0, off=servo_mid)
# pwm.set_pwm(channel=4, on=0, off=servo_mid)
# '''
