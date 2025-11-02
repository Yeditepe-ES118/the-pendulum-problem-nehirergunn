import numpy as np

g = 9.81

def find_period(L0, L1):
    for L in range(L0,L1+1):
        T = 2*np.pi*np.sqrt(L/g)
        print(f"When L = {L:4.1f} m, T = {T:4.1f} s")

    T0 = 2*np.pi*np.sqrt(L0 / g)
    T1 = 2*np.pi*np.sqrt(L1 / g)
    return T0, T1
find_period(2, 10)

