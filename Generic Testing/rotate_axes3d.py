'''
==================
Rotating a 3D plot
==================

A very simple animation of a rotating 3D plot.

See wire3d_animation_demo for another simple example of animating a 3D plot.
'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from sympy import zoo, oo, nan
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# load some test data for demonstration and plot a wireframe
#X, Y, Z = axes3d.get_test_data(0.1)

def f(x, y):
    #return np.sin(np.sqrt(x ** 2 + y ** 2))
    val = (x ** 2 / 500 ** 2) - (y ** 2 / 500 ** 2)

    # not working
    #val = (x**2/4) - (y**2/4)
    #return val.map(lambda x: np.nan if x < 0 else x)

x = np.linspace(-6, 6, 50)
y = np.linspace(-6, 6, 50)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
#ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
#
# rotate the axes and update
#for angle in range(0, 360):
#    ax.view_init(30, angle)
#    plt.draw()
#    plt.pause(.001)
ax.view_init(30, 180)
plt.show()
