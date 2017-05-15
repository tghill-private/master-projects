#!/usr/bin/env python

"""
Plots constant energy contours and x(t)
"""

import numpy as np
from matplotlib import pyplot as plt

m = 1.
k = 1.
a = 1.

energy_levels = np.array([0, 0.125*k*a*a, 0.25*k*a*a, 0.5*k*a*a, 0.75*k*a*a])
energy_labels = ['', 'Oscillatory', '', 'Critical', 'Free']

def x_dot(X, E):
  xd_2 = -k*(X**2)/m + 0.5*k*(X**4)/(a*a*m) + E
  xd_2[xd_2<0]=0
  xd = np.sqrt(xd_2)
  return xd

def energy_contours(energy_levels, figname, xmin=-2*a, xmax=2*a):
    X = np.linspace(xmin, xmax, 100)
    fig, ax = plt.subplots()
    for E, label in zip(energy_levels, energy_labels):
        xdot = x_dot(X, E)
        contour = ax.plot(X, xdot, label='E = {}'.format(E))

        E_middle = xdot[int(len(xdot)//2)]
        xpt = X[int(len(xdot)//2)]

        ax.text(xpt, E_middle, label)

    ax.legend()

    ax.set_xlabel('$x(t)$')
    ax.set_ylabel('$\dot{x}(t)$')
    ax.set_title('Constant Energy Contours ($x$, $\dot{x}$)')
    ax.grid()
    fig.savefig(figname, dpi=600)

def x(T, figname):
    b = np.sqrt(2*k/m)
    X = (1-np.exp(-b*T))/(np.exp(-b*T)+1)

    fig, ax = plt.subplots()
    ax.plot(T, X)
    ax.grid()

    ax.set_xlabel('$t$')
    ax.set_ylabel('$x$')

    ax.set_title('$x(t)$')

    fig.savefig(figname, dpi=600)

def U(X, figname):
    u = 0.5*k*X*X - 0.25*k*(X**4)/(a*a)

    fig, ax = plt.subplots()
    ax.plot(X, u, color='b')

    ax.grid()
    ax.set_ylabel('$U(x)$')
    ax.set_xlabel('$x$')

    ax.plot([-a, 0, a], [0.25*k*a*a, 0, 0.25*k*a*a], marker='.', ls='', color='b')

    ax.text(a, 0.25*k*a*a, '$(a, {ka^2}/4)$')
    ax.text(-a, 0.25*k*a*a, '$(-a, {ka^2}/4)$')
    ax.text(0, 0.1, '$(0,0)$')

    ax.set_title('Potential Energy $U(x)$')

    fig.savefig(figname, dpi=600)


if __name__ == '__main__':
  energy_contours(energy_levels, 'energy_contours.png')
#  x(np.linspace(0., 5., 100), 'x_t.png')
  U(np.linspace(-2., 2., 100), 'U_x.png')
