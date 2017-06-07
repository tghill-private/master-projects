import scipy.integrate
import numpy as np
from matplotlib import pyplot as plt

## Constants

m = 1.0
k = 1.0
e = 0.5
x0 = 1.

t = np.linspace(0, 6.3,  500)

K = np.array( [ [0, 0, 1., 0],
                [0, 0, 0., 1.],
                [-k/m*(1+e), e*k/m, 0, 0],
                [e*k/m, -k/m*(1+e), 0, 0] ])

psi_prime = lambda p, t:  np.dot(K, p.T)

psi_00 = np.array([x0, x0, 0, 0])
psi_01 = np.array([x0, -x0, 0, 0])
psi_02 = np.array([x0, np.sqrt(2)*x0, 0, 0])

IC = np.array([psi_00, psi_01, psi_02])



for i,psi_0 in enumerate(IC):
    fig, ax = plt.subplots()
    figname = 'a5q%s.png' % i
    psi = scipy.integrate.odeint(psi_prime, psi_0, t)
    ax.plot(t, psi[:,0], color='b', label='x1')
    ax.plot(t, psi[:,1], color='r', label='x2')
    ax.set_xlabel('t')
    ax.set_ylabel('x')
    ax.legend()
    fig.savefig(figname, dpi=500)
    plt.clf()
