'''
Servo class for generic servos controlled with Adafruit PCA9685 drivers.

Note: This license has also been called the "New BSD License" or "Modified BSD License". See also the 2-clause BSD License.

Copyright 2017 kiyoshigawa

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

import time
import Adafruit_PCA9685

#Default values for variables below - update as needed for your servos.
DEFAULT_THETA_MIN = -90
DEFAULT_THETA = 0
DEFAULT_THETA_MAX = 90
DEFAULT_PULSE_MID = 1500

#update these based on servo brand/type (values in us).
DEFAULT_PULSE_MIN = 560
DEFAULT_PULSE_MAX = 2440

#initializes with default values for Hi-Tec HS-322HD servos, feel free to change defaults to your servo, or set manually for the project.
class servo:

  #This is a variable to track the used controllers and channels of all active servos.
  used_channels=[]

  #this is a list of all the created Servo class objects, for use by the init and update functions.
  servo_list = []

  #this is a variable for tracking the number of currently active initialized servos in the servo_list.
  num_active = 0

  #This is a set of the channel numbers generated during initialization to facilitate creating the controller objects.
  active_controller_channels = set([])

  #this is a list variable foir storing the Adafruit_PCA9685 objects that will control the servos.
  controllers = []

  def __init__(self, controller, channel, servo_constant, theta=None, theta_default=DEFAULT_THETA, pulse_min=DEFAULT_PULSE_MIN, pulse_max=DEFAULT_PULSE_MAX, pulse_mid=DEFAULT_PULSE_MID):

    #controller is hex address if 12c controller for adafruit library. Typically 0x40
    self.controller = controller
    #channel is the channel of the servo on that controller. Will be integer from 0-15.
    self.channel = channel
    #servo_constant is the number of degrees per us of pulse length for the servo. For the HS-322HD, this is 0.106.
    self.servo_constant = servo_constant
    #theta_min is the lowest theta value the servo can go to in degrees. Any values lower than this will be set to this value.
    self.theta_min = theta_min
    #theta_default is the mid-point degree value for the servo. All offsets are calculated from this based on the servo_constant and pulse_mid.
    self.theta_default = theta_default
    #theta_max is the highest theta value the servo can go to in degrees. Any values higher than this will be set to this value.
    self.theta_max = theta_max
    #this is the value where the servo is at the dead center of its range of motion. Should be tested for empirically in an ideal world. Default was average of the HS-322HD servos I tested.
    self.pulse_mid = pulse_mid

    #set theta up as a mutable property with a default value of 0.
    if theta is None:
      self._theta = DEFAULT_THETA
    else:
      self._theta = theta

    #Now to set some additional properties that can be calculated from the user-set values above:
    
    #This calculates the minimum pulse width for this servo.
    self.pulse_min = DEFAULT_PULSE_MIN
    #This calculates the maximum pusle width for this servo.
    self.pulse_max = DEFAULT_PULSE_MAX
    #FIXME This calculates the pwm frequency for the controller, based on all the existing servo values on that controller. 
    #If it cannot find a pwm value that will work for all servos on the controller, an error will be raised.
    self.pwm_frequency = 350

    #As each class object is created, update the class variable used_channels with a controller channel pair, after verifying that it is not already in use:
    if len(servo.used_channels) == 0:
      servo.used_channels.append( (controller, channel) )
    else:
      for uc in servo.used_channels:
        if uc[0] == controller and uc[1] == channel:
          raise ValueError("Error: controller/channel combination is a duplicate, make sure every servo has a unique controller/channel combination!")
      servo.used_channels.append( (controller, channel) )

    #update the servolist with this newest instance.
    servo.servo_list.append(self)


  #this will initialize the PCA9685 for first time running and set all channels to the current theta for all currently initialized controllers contained in the used_channels class variable.
  #You will only need to initialize the class once, unless you add additional servo controllers later.
  @classmethod
  def initialize(cls):
    #first make sure there are servos to initialize.
    if len(cls.used_channels) == 0:
      raise ValueError("Error: Unable to initialize servos, as no servo objects have been created. Please create all servo objects and then run the initialize.")
    else:
      #reset variables so this will work properly.
      cls.num_active = 0
      cls.controllers = []
      cls.active_controller_channels = set([])

      print("Initializing Servos...")
      #this will iterate through the servo_list and set up the actual pwm Adafruit_PCA9685 objects for running each servo.
      for s in cls.servo_list:
        #This only adds to the set if it is not in the set already.
        cls.active_controller_channels.add( s.controller )
        #increment number of active controllers once activation is complete
        cls.num_active = cls.num_active+1
      print(cls.active_controller_channels)
      #create the Adafruit_PCA9685 objects on the correct controller as needed and add to the active_controller_channels.
      for c in cls.active_controller_channels:
        cls.controllers.append( Adafruit_PCA9685.PCA9685(c) )
        print( cls.controllers )
      #once the objects are created, run the update class method to that they will move to the correct theta positions.
      cls.update()



  #this will update the the PCA9685 for all currently created servos to their current theta values.
  @classmethod
  def update(cls):
    #check to see if used_channels is empty and error if it is:
    if len(cls.used_channels) == 0:
      raise ValueError("Error: No servos have been initialized on any channel! Cannot run update.")
    #FIXME Iterate through all Servo class objects and set the controller channel pwm to the required pulses.
  
  #Theta property functions
  @property
  def theta(self):
    return self._theta

  @theta.setter
  def theta(self, theta):
    if theta < self.theta_min:
      self._theta = self.theta_min
    if theta > self.theta_max:
      self._theta = self.theta_max
    else:
      self._theta = theta

  @theta.deleter
  def theta(self):
    del self._theta
