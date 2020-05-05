# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:18:36 2020

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt
 
pos = np.zeros((2))  #x,y
vel = np.array([10.0,20.0])
g =  np.array([0,-9.80665])
t = 0.01
n = 400
result = np.zeros((n,2))


for i in range(n):
    pos += vel*t
    vel += g*t
    result[i] = pos

plt.plot(result[:,0],result[:,1])
plt.show()
