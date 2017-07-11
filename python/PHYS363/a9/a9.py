import numpy as np
import scipy.integrate
from matplotlib import pyplot as plt

"""
Question 1
"""

def q1():
    m = 1.
    k = 1.
    a = 1.

    w = np.sqrt(k/m)
    r0 = (6./5.)*a
    w0 = w*np.sqrt(1 - (a/r0))
    wr = w*np.sqrt(4 - 3*(a/r0))

    V0 = 0.5*k*(2*r0-a)*(r0-a)
    T = 2*np.pi/w

    y0 = np.array([1.1*r0, 0, 0, m*r0*r0*w0])

    t = np.linspace(0, 3*T, 1000)

    def psi_prime(psi, t):
        r, x, pr, px = psi
        r_dot = pr/m
        x_dot = px/(m*r*r)
        pr_dot = ((px*px)/(m*(r**3))) - (k*(r - a))
        px_dot = 0.
        return np.array([r_dot, x_dot, pr_dot, px_dot])

    Y = scipy.integrate.odeint(psi_prime, y0, t)

    fig, ax = plt.subplots()

    ax.plot( t/T, (Y[:,0]-r0)/r0)
    ax.set_xlabel('$t/T$')
    ax.set_ylabel('$(r-r_0)/r_0$')
    ax.grid()
    fig.savefig('a9q1_01.png', dpi=500)

    fig2, ax2 = plt.subplots()
    x = Y[:,0]*np.cos(Y[:,1])
    y = Y[:,0]*np.sin(Y[:,1])
    ax2.plot(x/r0, y/r0)
    ax2.plot(np.cos(Y[:,1]), np.sin(Y[:,1]), c='k')
    ax2.set_xlabel('$x/r_0$')
    ax2.set_ylabel('$y/r_0$')
    ax2.grid()
    fig2.savefig('a9q1_02.png', dpi=500)

def q2():
    X = np.linspace(-2, 3, 100)
    veff = -3*(X**2) + 2*(X**3)

    figb, axb = plt.subplots()
    axb.plot(X, veff)
    axb.set_xlabel('$x/x_1$')
    axb.set_ylabel('$V/V_1$')
    axb.set_title('Effective Potential vs. x distance')
    axb.grid()

    figb.savefig('a9q2_01.png', dpi=500)

    figc, axc = plt.subplots()

    R = np.array([-2., -1., 0., 1., 2.])
    x = np.linspace(-2, 10, 100)
    for r in R:
        Y = r + 3*(x**2) - 2*(x**3)
        xp = x[Y>=0]
        Y = Y[Y>=0]

        axc.plot(xp, Y, c='b')
        axc.plot(xp, -Y, c='b')

    axc.set_xlabel('$x$')
    axc.set_ylabel('$p_x$')
    figc.savefig('a9q2_02.png', dpi=500)

def q3():
    X = np.linspace(-1.5, 1.5, 100)
    p = np.array([0., 0.5, 1., 1.5, 2.])

    def v_eff(x, p):
        return 0.5*(p**2)/(1+(x**2)) + (0.5*(x**2))

    figb, axb = plt.subplots()
    for p_0 in p:
        axb.plot(X, v_eff(X, p_0), label=p_0)

    axb.legend()
    axb.set_xlabel('$x/a$')
    axb.set_ylabel('$V_{eff}/V_c$')

    axb.set_title('$V_{eff}(x)$')

    figb.savefig('a9q3_01.png', dpi=500)

    m = 1.
    k = 1.

    figc, axc = plt.subplots()
    for p in np.array([0., 0.5, 1., 2.]):
        for h in np.array([0.5, 1., 1.5]):
            px = np.sqrt(h/(2*m) + v_eff(X, p))
            axc.plot(X, px)
            axc.plot(X, -px)

    figc.savefig('a9q3_02.png', dpi=500)


if __name__ == '__main__':
    q1()
