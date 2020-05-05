# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:37:45 2020

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

pos1 = np.array([10.0,0])
pos2 = np.array([0.0,0])

vel1 = np.array([0,0.5])
vel2 = np.array([0,0.0])

M = 5*10**10
m = 5*10**10
G = 6.67*10**-11
n = 100000
t = 0.1
result1 = np.zeros((n,2))
result2 = np.zeros((n,2))

for i in range(n):
    k11  = t*vel1
    vk11 = -t*G*M*(pos1-pos2)/(np.linalg.norm(pos1-pos2))**3
    k12  = t*vel2
    vk12 = -t*G*M*(pos2-pos1)/(np.linalg.norm(pos2-pos1))**3
    
    k21  = t*(vel1+vk11/2)
    vk21 = -t*G*M*(pos1+k11/2-pos2-k12/2)/(np.linalg.norm(pos1+k11/2-pos2-k12/2))**3
    k22  = t*(vel2+vk12/2)
    vk22 = -t*G*M*(pos2+k12/2-pos1-k11/2)/(np.linalg.norm(pos2+k12/2-pos1-k11/2))**3
    
    k31  = t*(vel1+vk21/2)
    vk31 = -t*G*M*(pos1+k21/2-pos2-k22/2)/(np.linalg.norm(pos1+k21/2-pos2-k22/2))**3
    k32  = t*(vel2+vk22/2)
    vk32 = -t*G*M*(pos2+k21/2-pos1-k21/2)/(np.linalg.norm(pos2+k22/2-pos1-k21/2))**3
    
    k41  = t*(vel1+vk31)
    vk41 = -t*G*M*(pos1+k31-pos2-k32)/(np.linalg.norm(pos1+k31-pos2-k32))**3
    k42  = t*(vel1+vk32)
    vk42 = -t*G*M*(pos2+k32-pos1-k31)/(np.linalg.norm(pos2+k32-pos1-k31))**3
    
    pos1 += (k11+2*k21+2*k31+k41)/6
    vel1 += (vk11+2*vk21+2*vk31+vk41)/6
    pos2 += (k12+2*k22+2*k32+k41)/6
    vel2 += (vk12+2*vk22+2*vk32+vk42)/6
    
    result1[i] = pos1
    result2[i] = pos2
    
plt.plot(result1[:,0]-(result1[:,0]+result2[:,0])/2,result1[:,1]-(result1[:,1]+result2[:,1])/2)
plt.plot(result2[:,0]-(result1[:,0]+result2[:,0])/2,result2[:,1]-(result1[:,1]+result2[:,1])/2)
plt.show()
