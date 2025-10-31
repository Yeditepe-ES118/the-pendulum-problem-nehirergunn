# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 01:34:56 2025

@author: aergu
"""

import numpy as np 
def find_period(L0, L1):
    g=9.81 #gravity in m/s**2
    T0= 2*np.pi*np.sqrt(L0/g)  # period for L0
    T1 = 2*np.pi*np.sqrt(L1/g)  # period for L1

    for L in range(L0, L1+1):
        T = 2*np.pi*np.sqrt(L/g)
        print("When L = %4.1f m, T = %4.1f s" % (L, T))
    
    return T0, T1

