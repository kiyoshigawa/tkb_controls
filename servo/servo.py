#Servo class for generic servos controlled with Adafruit PCA9685 drivers.

import time
import Adafruit_PCA9685

#initializes with default values for Hi-Tec HS-322HD servos, feel free to change defaults to your servo, or set manually for the project.
class servo:

  #This is a variable to track the used controllers and channels of all active servos.
  used_channels=[]

  #this is a list of all the created Servo class objects, for use by the init and update functions.
  servo_list = []

  def __init__(self, controller, channel, servo_constant, theta=None, theta_min=-90, theta_mid=0, theta_max=90, pulse_mid=2200):

    #controller is hex address if 12c controller for adafruit library. Typically 0x40
    self.controller = controller
    #channel is the channel of the servo on that controller. Will be integer from 0-15.
    self.channel = channel
    #servo_constant is the number of degrees per us of pulse length for the servo. For the HS-322HD, this is 0.106.
    self.servo_constant = servo_constant
    #theta_min is the lowest theta value the servo can go to in degrees. Any values lower than this will be set to this value.
    self.theta_min = theta_min
    #theta_mid is the mid-point degree value for the servo. All offsets are calculated from this based on the servo_constant and pulse_mid.
    self.theta_mid = theta_mid
    #theta_max is the highest theta value the servo can go to in degrees. Any values higher than this will be set to this value.
    self.theta_max = theta_max
    #this is the value where the servo is at the dead center of its range of motion. Should be tested for empirically in an ideal world. Default was average of the HS-322HD servos I tested.
    self.pulse_mid = pulse_mid

    #set theta up as a mutable property with a default value of 0.
    if theta is None:
      self._theta = 0
    else:
      self._theta = theta

    #Now to set some additional properties that can be calculated from the user-set values above:
    
    #FIXME This calculates the minimum pulse width for this servo.
    self.pulse_min = 0
    #FIXME This calculates the maximum pusle width for this servo.
    self.pulse_max = 4096
    #FIXME This calculates the pwm frequency for the controller, based on all the existing servo values on that servo. 
    #If it cannot find a pwm value that will work for all servos on the controller, an error will be raised.
    self.pwm_frequency = 350

    #As each class is created, update the class variable used_channels with a controller channel pair, after verifying that it is not already in use:
    if len(used_channels) == 0:
      used_channels.append( (controller, channel) )
    else:
      for uc in used_channels:
        if uc[0] == controller and uc[1] == channel:
          raise ValueError("Error: controller/channel combination is a duplicate, make sure every servo has a unique controller/channel combination!")
        else:
          used_channels.append( (controller, channel) )

    #update the servolist with this newest instance.
    servo_list.append(self)

  #this will update the the PCA9685 for all currently created servos to their current theta values.
  @classmethod
  def update(cls):
    #check to see if used_channels is empty and error if it is:
    if len(used_channels) == 0:
      raise ValueError("Error: No servos have been initialized on any channel! Cannot run update.")
    #Iterate through all Servo class objects and set the controller channel pwm to the required pulses.
  
  #this will initialize the PCA9685 for first time running and set all channels to the current theta for all currently initialized controllers contained in the used_channels class variable.
  #You will only need to initialize the class once, unless you add additional servo controllers later.
  @classmethod
  def initialize(cls):
    #First create class objects for the used controllers:
    pass
    #once the objects are created, run the update class method to that they will move to the correct theta positions.

  #Theta property functions
  @property
  def theta(self):
    return self._theta

  @theta.setter
  def theta(self, theta):
    if theta < self.theta_min:
      self._theta = self.theta_min
    if theta < self.theta_max:
      self._theta = self.theta_max
    else:
      self._theta = theta

  @theta.deleter
  def theta(self):
    del self._theta

