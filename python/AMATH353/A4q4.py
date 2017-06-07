"""

Finite difference method for solving PDES

"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

xres = 100
tres = 100

X = np.linspace(-10, 10, xres)
T = np.linspace(0, 5, tres)

h = float(T[1]-T[0])
k = float(X[1]-X[0])

U = np.zeros((xres, tres))

# Boundary Conditions
U[0] = np.exp(-X*X)

Xmesh, Tmesh = np.meshgrid(X, T[::-1])

for j in np.arange(xres):
    x = j
    x2 = j if j==xres-1 else j+1
    for n in np.arange(tres-1):
        t = n
        Unew = U[n, j] + (k*np.cos(X[x])) - ((k/h)*(U[n, x2] - U[n, x]))
        U[n+1, j] = Unew

fig = plt.figure()
ax = fig.gca(projection = '3d')


ax.plot_surface(Xmesh, Tmesh, U)

fig.savefig('pdesolve.png')
