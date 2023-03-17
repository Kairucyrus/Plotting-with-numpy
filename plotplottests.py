# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:25:33 2023

@author: Kairu Cyrus
"""

import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(-10,10,100) # Start point -10, stop-point 10(excluded unless endpoint=True), 100 samples
y= np.sin(x)
plot=plt.plot(x,y)
plot.show()
  
  
  
