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
    return T0, T1