# This file will allow you to specify a servo controller, channel, constant, and mid-pulse pwm,
# Then fine-tune that mid-pulse pwm.
# Once that is set, you can adjust to find the max and min angle range.

import time
import servo
import curses
from curses import wrapper

# A simple debug iprint function:
DEBUG = True


def log(s):
    if DEBUG:
        print(s)
# Some basic definitions for use below
DEFAULT_CONTROLLER = 0x40
DEFAULT_CHANNEL = 0
DEFAULT_PULSE_LENGTH = 1500
DEFAULT_THETA = 0
DEFAULT_SERVO_CONSTANT = 0.106
DEFAULT_THETA_MIN = -90
DEFAULT_THETA_MAX = 90
DEFAULT_INCREMENT = 1.0


# First get basic info:
# This block is for the controller address in hex:
while True:
    try:
        controller_input_string = input("What address is the controller for this servo on in hex? [{}]".format(hex(DEFAULT_CONTROLLER)))
        # Use default value if left blank.
        if controller_input_string == '':
            controller = hex(DEFAULT_CONTROLLER)
            break
        # Check to see if it's formatted as '0x#####' and set a hex value if it is.
        elif controller_input_string[0] is '0' and controller_input_string[1] is 'x':
            controller = hex(int(controller_input_string[2:], 16))
            break
        else:
            raise ValueError
    except ValueError:
        print("The value must be a hex string of format 0x##.")


# This block is for the controller channel the servo in question is on:
while True:
    try:
        channel_input_string = input("What channel [0-15] is the servo on? [{}]".format(DEFAULT_CHANNEL))
        # Use default value if left blank.
        if channel_input_string == '':
            channel = int(DEFAULT_CHANNEL)
            break
        # Save an integer value if entered correctly. Will error if not an int.
        else:
            channel = int(channel_input_string)
            if(channel > 15):
                raise ValueError
            break
    except ValueError:
        print("The value must be an integer below from 0-15.")


# This block is for setting the default pulse length:
while True:
    try:
        pulse_length_input_string = input("What should be the initial pulse length in microseconds (us)? [{}]".format(DEFAULT_PULSE_LENGTH))
        # Use default value if left blank.
        if pulse_length_input_string == '':
            pulse_length = int(DEFAULT_PULSE_LENGTH)
            break
        # Save an integer value if entered correctly. Will error if not an int.
        else:
            pulse_length = int(pulse_length_input_string)
            break
    except ValueError:
        print("The value must be an integer.")


# This block is for setting the default theta:
while True:
    try:
        theta_input_string = input("What value for theta corresponds to the pulse length just entered? [{}]".format(DEFAULT_THETA))
        # Use default value if left blank.
        if theta_input_string == '':
            theta = int(DEFAULT_THETA)
            break
        # Save a float value if entered correctly. Will error if not a float.
        else:
            theta = float(theta_input_string)
            if theta < -180.0 or theta > 180.0:
                raise ValueError
            break
    except ValueError:
        print("The value must be a number between -180.0 and 180.0.")


# This block is for setting the default servo constant:
while True:
    try:
        servo_constant_input_string = input("What is the servo constant in degrees per us? [{}]".format(DEFAULT_SERVO_CONSTANT))
        # Use default value if left blank.
        if servo_constant_input_string == '':
            servo_constant = float(DEFAULT_SERVO_CONSTANT)
            break
        # Save an integer value if entered correctly. Will error if not an int.
        else:
            servo_constant = float(servo_constant_input_string)
            break
    except ValueError:
        print("The value must be a number.")

# A message to let you know it's about to boot up the servo and go into editing mode:
print("Initializing servo with input values and entering test mode...")
time.sleep(1)

s = servo.servo(controller=controller, channel=channel, servo_constant=servo_constant, theta=theta, default_pulse=pulse_length, theta_min=DEFAULT_THETA_MIN, theta_max=DEFAULT_THETA_MAX)
s.update()

# This is the entire screen object used by curses:
stdscr = curses.initscr()

# This is the window where stuff will happen:
win_x_corner = 0
win_y_corner = 0
win_lines = 20
win_cols = 69
win = curses.newwin(win_lines, win_cols, win_x_corner, win_y_corner)

theta_min=DEFAULT_THETA_MIN
theta_max=DEFAULT_THETA_MAX

increment = DEFAULT_INCREMENT

last_key_press = ''


# initialize the screen:
def main(stdscr):
    global controller
    global channel
    global pulse_length
    global theta
    global servo_constant
    global s
    # Clear Screen:
    stdscr.clear()
    stdscr.refresh()

    # loop through the function until esc key is pressed:
    while True:
        print_servo_info()

        # Print the update screen
        last_key_press = stdscr.getkey()

        # Check inputs and do stuff.
        if last_key_press == 'q':
            break
        if last_key_press == 'g':
            # Increment servo_constant up and re-init.
            servo_constant = servo_constant + increment
            del s
            s = servo.servo(controller=controller, channel=channel, servo_constant=servo_constant, theta=theta, default_pulse=pulse_length, theta_min=DEFAULT_THETA_MIN, theta_max=DEFAULT_THETA_MAX)
            s.update()
        if last_key_press == 'b':
            # Increment servo_constant down and re-init.
            servo_constant = servo_constant - increment
            del s
            s = servo.servo(controller=controller, channel=channel, servo_constant=servo_constant, theta=theta, default_pulse=pulse_length, theta_min=DEFAULT_THETA_MIN, theta_max=DEFAULT_THETA_MAX)
            s.update()
        if last_key_press == 'a':
            # Increment pulse_length up
            pass
        if last_key_press == 'z':
            # Increment pulse_length down
            pass
        if last_key_press == 's':
            # Increment theta up
            pass
        if last_key_press == 'x':
            # Increment theta down
            pass
        if last_key_press == 'd':
            # Increment theta_min up
            pass
        if last_key_press == 'c':
            # Increment theta_min down
            pass
        if last_key_press == 'f':
            # Increment theta_max up
            pass
        if last_key_press == 'v':
            # Increment theta_max down
            pass
        if last_key_press == 'h':
            # Increase increment by 10x
            pass
        if last_key_press == 'n':
            # Decrease increment by 10x
            pass
        if last_key_press == 'r':
            # Set current pulse_length to default and re-init.
            pass
        if last_key_press == 't':
            # Set current theta to default and re-init.
            pass
        if last_key_press == 'y':
            # Set current theta to Theta_Max
            pass
        if last_key_press == 'u':
            # Set current Theta to Theta_Min
            pass
        if last_key_press == 'e':
            # Enable servo
            pass
        if last_key_press == 'w':
            # Disable Servo
            pass

        #Refresh Every Loop
        stdscr.refresh()


#This is a function for printing current servo parameters.
def print_servo_info():
    win.border('|','|','-','-','+','+','+','+')

    win.addstr( 2, 2, "Servo Info:")
    win.addstr( 3, 2, "Controller Address: {:>8}".format(controller))
    win.addstr( 4, 2, "Controller Channel: {:>8}".format(channel))
    win.addstr( 5, 2, "Servo Constant:     {:>8} ( g / b )".format(servo_constant))
    win.addstr( 6, 2, "+---------------+---------------+---------------+---------------+")
    win.addstr( 7, 2, "|{:^15}|{:^15}|{:^15}|{:^15}|".format("Current Pulse*", "Current Theta", "Theta Min", "Theta Max"))
    win.addstr( 8, 2, "|{:^15}|{:^15}|{:^15}|{:^15}|".format("( a / z )", "( s / x )", "( d / c )", "( f / v )"))
    win.addstr( 9, 2, "+---------------+---------------+---------------+---------------+")
    win.addstr(10, 2, "|{:^15}|{:^15}|{:^15}|{:^15}|".format(pulse_length, theta, theta_min, theta_max))
    win.addstr(11, 2, "+---------------+---------------+---------------+---------------+")
    win.addstr(12, 2, "Incrementing variables by: {} ( h / n )".format(increment))
    win.addstr(13, 2, "Set pulse to default with 'r'")
    win.addstr(14, 2, "Set Theta to default with 't'")
    win.addstr(15, 2, "Set Theta to Theta_min and Theta_max to theta with 'y' and 'u'")
    win.addstr(16, 2, "Enable servo with 'e' and disable servo with 'w'")
    win.addstr(win_lines-2, 2, "Press 'q' to quit.")
    win.refresh()


wrapper(main)
