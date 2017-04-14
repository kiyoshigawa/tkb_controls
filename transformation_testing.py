'''
Date: 2017-04-12
Author: kiyoshigawa
This is a file for testing basic forward kinematics equations using DH parameters. Hopefully it will eventually lead to both understanding and useful robotics controls.
'''

import numpy as np
from math import *

class DH():
  def __init__(self, a, d, alpha, theta, min_d, max_d, min_theta, max_theta):
    self.a = a
    self.d = d
    self.alpha = alpha
    self.theta = theta
    self.min_d = min_d
    self.max_d = max_d
    self.min_theta = min_theta
    self.max_theta = max_theta

    def t_fwd(dh):
#this will return a transformation matrix array based on the array of 4 DH parameter numbers that were input.
      trans_matrix = np.matrix([
          [cos(dh.theta), -sin(dh.theta)*cos(dh.alpha), sin(dh.theta)*sin(dh.alpha), dh.a*cos(dh.theta)],
          [sin(dh.theta), cos(dh.theta)*cos(dh.alpha), -cos(dh.theta)*sin(dh.alpha), dh.a*sin(dh.theta)],
          [0, sin(dh.alpha), cos(dh.alpha), dh.d],
          [0,0,0,1]
      ])
return(trans_matrix)

# Define DH parameters for chain
  T0_dh = DH(0,         -1.001810, radians(-90),  radians(45 ), -1.001810, -1.001810, radians(  45), radians(  45))
  T1_dh = DH(0,          6.692882, radians( 90),  radians(0  ),  6.692882,  6.692882, radians( -45), radians(  45))
  T2_dh = DH(1.790900,  -0.056849, radians(-90),  radians(90 ), -0.056849, -0.056849, radians(   0), radians( 180))
  T3_dh = DH(4.010076,  -0.109910, radians( 0 ),  radians(0  ), -0.109910, -0.109910, radians( -60), radians(  90))
  T4_dh = DH(0,          0,        radians(-90),  radians(0  ),  0,         0,        radians(-120), radians(  60))
  T5_dh = DH(0,          7.332779, radians(-90),  radians(135),  7.332779,  7.332779, radians(  45), radians( 225))
T6_dh = DH(1,          0,        radians( 0 ),  radians(-90),  0,         0,        radians(   0), radians( 360))

  trans_chain_dh = [T0_dh, T1_dh, T2_dh, T3_dh, T4_dh, T5_dh, T6_dh]

print(trans_chain_dh)

Tn = np.identity(4)
  i = 0;

  for Tmat in trans_chain_dh:
Ti = t_fwd(Tmat)
#print("Ti:",i,"\n",Ti)
Tn = np.matmul(Tn,Ti)
#print("Tn:",i,"\n",Tn)
  disp = np.array([Tn[0,3],Tn[1,3],Tn[2,3]])
mag = sqrt(disp[0]*disp[0]+disp[1]*disp[1]+disp[2]*disp[2])
  print("Vector: ",disp, " Magnitude: ", mag)
  i=i+1

