"""
Plots characteristic curves and how the solution evolves
along the characteristic curves
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plot the entire manifold first:
# X = np.linspace(0, 5, 100)
# T = np.linspace(0, 5, 100)
#
# X, T = np.meshgrid(X, T)
#
# Z = 1./(1+((X-2*T)/3.)**2) * np.exp(-(X+T)/3.)
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# surf = ax.plot_surface(X, T, Z, linewidth=0.)
#
# fig.savefig('Surface_plot.png')


# Plot the solutions along specific lines

fig = plt.figure()
ax = fig.gca(projection = '3d')

T = np.array([-2, -1, 0, 1, 2])
S = np.linspace(0, 5, 100)

x0 = np.linspace(T[0], T[-1], 100)
y0 = np.linspace(-T[0], -T[-1], 100)
V0 = 1/(1+x0**2)

ax.plot(x0, y0, V0, label='Initial Conditions')

t = np.array([(S + T0)/3. for T0 in T])

V = lambda t: (1./(1+t**2)) * np.exp(-S)

for t0 in T:
    z = V(t0)
    x = (2*S + t0)
    y = (S - t0)

    ax.plot(x, y, z, label=t0)
    ax.plot(x, y, 0, ls=':', color='k')

    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('z')

#    ax.legend()

    ax.view_init(elev=30, azim=-70)

fig.savefig('characteristics.png', dpi=600)
