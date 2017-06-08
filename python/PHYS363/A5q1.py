"""
Phys 363 Assignment 5, Question 1

Solve the problem of the 2 coupled oscillators numerically,
and compare the numerical and analytic solutions to the problem.

Plot x1(t) vs. x2(t), as well as the difference between
(x1(t) - x2(t)) for numerical and analytic solutions
"""

import scipy.integrate
import numpy as np
from matplotlib import pyplot as plt

## Constants

m = 1.0
k = 1.0
e = 0.5
x0 = 1.

t = np.linspace(0, 15,  500)

## Analytic Solution
w1 = np.sqrt(k/m)
w2 = np.sqrt(k/m*(1+2*e))

## Normal modes
x_1 = np.array([np.cos(w1*t),np.cos(w1*t)])     # Slow Mode
x_2 = np.array([np.cos(w2*t), -np.cos(w2*t)])   # Fast Mode

# Coefficients of the superposition for the analytic solutions
superpositions = ( (x0, 0), (0, x0), (0.5*(1+np.sqrt(2)), 0.5*(1-np.sqrt(2))) )


K = np.array( [ [0, 0, 1., 0],
                [0, 0, 0., 1.],
                [-k/m*(1+e), e*k/m, 0, 0],
                [e*k/m, -k/m*(1+e), 0, 0] ])

psi_prime = lambda p, t:  np.dot(K, p.T)

## Initial Conditions
psi_00 = np.array([x0, x0, 0, 0])
psi_01 = np.array([x0, -x0, 0, 0])
psi_02 = np.array([x0, np.sqrt(2)*x0, 0, 0])

IC = np.array([psi_00, psi_01, psi_02])

fig,axes = plt.subplots(nrows=len(IC), ncols=2, figsize=(8,10))
axes[0,1].set_title('Numerical - Analytic Solution')
axes[0,0].set_title('Numerical and Analytic')

for i,psi_0 in enumerate(IC):
    psi = scipy.integrate.odeint(psi_prime, psi_0, t)
    axes[i,0].plot(psi[:,1], psi[:,0], color='b', label='Numerical Solution')
    a, b = superpositions[i]
    xs1, xs2 = a*x_1 + b*x_2
    error = (psi[:,1]-psi[:,0]) - (xs2-xs1)
    axes[i,0].plot(xs2, xs1, color='k', label='Analytic Solution', ls=':')
    axes[i,1].plot(t, error)
    axes[i,0].set_xlabel('$x_2(t)$')
    axes[i,0].set_ylabel('$x_1(t$)')
    # axes[i,0].legend()
    axes[i,1].set_xlabel('$t$')
    axes[i,1].set_ylabel('$x_1(t) - x_2(t)$')

plt.tight_layout()
fig.savefig('coupled_oscillator_x1_x2.png', dpi=500)
