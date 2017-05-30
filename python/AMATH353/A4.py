"""
AMATH 353 Assignment 4, Question 3
"""

## Question 3

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

T = np.array([-1, -0.5, 0, 0.5, 1., 5.])

t = np.linspace(-5, 5, 100)
X = np.array([(T0)**3/((1+3*t*(T0**3))) for T0 in T])

X = np.sign(X)*(np.abs(X)**(1./3.))


fig, ax = plt.subplots()
for (t_0, x) in zip(T, X):
    ax.plot(x, t, label="T = %s" % t_0)

ax.grid()
ax.set_ylim(t[0], t[-1])
ax.legend(loc=2)
plt.savefig('A4q3.png', dpi=600)
plt.clf()
