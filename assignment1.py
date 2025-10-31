# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 01:34:56 2025

@author: aergu
"""
import numpy as np

def find_period(L0, L1):
    g = 9.81  # gravity (m/s^2)
    
    T0 = 2 * np.pi * np.sqrt(L0 / g)  # period at L0 (s)
    T1 = 2 * np.pi * np.sqrt(L1 / g)  # period at L1 (s)
    
    for L in range(L0, L1 + 1):
        T = 2 * np.pi * np.sqrt(L / g)  # period at L (s)
        # no print here
    
    return T0, T1

if __name__ == "__main__":
    L0, L1 = 2, 10
    
    T0, T1 = find_period(L0, L1)

    g = 9.81
    for L in range(L0, L1 + 1):
        T = 2 * np.pi * np.sqrt(L / g)
        print("When L = %.1f m, T = %.1f s" % (L, T))