import numpy as np

A_k = lambda k: np.abs(25 * np.pi / (6.25 * np.pow(np.pi, 2) - 6.25 * np.pow(np.pi*k, 2) ) * np.sin(k * np.pi / 2))
def F_k (k):
    if np.sin(k * np.pi / 2) > 0:
        val = -0.5*k*np.pi
    else:
        val = -0.5*k*np.pi + np.pi
    return 0 if val % (2*np.pi) == 0 else val

print(f"{'k':<5}{'omega':<10}{'A_k':<20}{'F_k':<20}")
print("-" * 45)
for k in range(0, 8):
    print(f"{k:<5}{2.5*k:<10}{A_k(k):<20.5f}{F_k(k):<20.5f}")