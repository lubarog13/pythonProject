import numpy as np
A = lambda k: 25 * np.pi / (6.25 * np.pow(np.pi, 2) - 6.25 * np.pow(np.pi*k, 2) ) * np.cos(k * np.pi / 2)
A_k = lambda k: np.abs(A(k))
def F_k (k):
    if A(k) >= 0:
        val = -0.5*k*np.pi
    else:
        val = -0.5*k*np.pi - np.pi
    return val
    # return -0.5*k*np.pi 

A_k_1 = lambda k: A_k(k) * (160 / np.sqrt(np.pow(2.5*np.pi*k, 4) - 136.39*np.pow(2.5*np.pi*k, 2) + 184900))

F_n = lambda k: -np.atan( (26.9 *2.5 *np.pi * k) / (430 - 6.25 * np.pow( np.pi* k, 2)))

print(f"{'k':<5}{'omega':<10}{'A_k':<20}{'F_k':<20}{'F_н':<20}{'A_k_1':<20}{'Ф_k':<20}")
print("-" * 45)
for k in range(0, 9):
    print(f"{k:<5}{2.5*k:<10}{A_k(k):<20.5f}{F_k(k):<20.5f}{F_n(k):<20.5f}{A_k_1(k):<20.5f}{F_n(k)+F_k(k):<20.5f}")