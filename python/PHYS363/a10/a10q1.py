#!/usr/bin/env python

"""

PHYS 363 Assignment 10 Question 1

"""

import numpy as np
import scipy.integrate
from matplotlib import pyplot as plt

def main():

    m = 1.
    w = 1.
    a = 1.

    A = np.array([  [0,  0,  1,  0],
                    [0,  0,  0,  1],
                    [w*w,0,  0,2*w],
                    [0,w*w,-2*w, 0] ])

    incs = (0.8, 0.9, 1., 1.1, 1.2)
    v0 = a*w

    psi_prime = lambda y,t: np.dot(A, y)

    t = np.linspace(0, 10, 1000)

    fig, (axd, axe) = plt.subplots(nrows=2, figsize=(6,10))

    for d in incs:
        y0_d = np.array([a, 0, 0, -d*v0])
        psi_d = scipy.integrate.odeint(psi_prime, y0_d, t)
        X, Y = psi_d.T[:2]
        axd.plot(X, Y, label='$\delta = %s$' % d)

        v = d*v0
        y0_e = np.array([a, 0, -v/np.sqrt(2), -v/np.sqrt(2)])
        psi_e = scipy.integrate.odeint(psi_prime, y0_e, t)
        X_e, Y_e = psi_e.T[:2]
        axe.plot(X_e, Y_e, label='$\delta = %s$' % d)

    axd.set_xlabel('$x$')
    axd.set_ylabel('$y$')
    axd.set_title('$\\vec{v_0} = -{\delta}a\omega\\vec{y}$')
    axd.legend()

    axe.set_title('$\\vec{v_0} = -{\delta}a\omega\\frac{(\hat{x} + \hat{y})}{\sqrt{2}}$')
    axe.set_xlabel('$x$')
    axe.set_ylabel('$y$')
    axe.legend()

    fig.savefig('a10.png', dpi = 500)

if __name__ == '__main__':
    main()
