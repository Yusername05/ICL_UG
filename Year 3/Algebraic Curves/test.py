'''
I want to plot the equation y^2 = x^3 + x + l on the porjective plane
so y^2z = x^3 + xz^2 + lz^3, if z = 0, then we must have x = 0 so [0,1,0] is the only missing point
if z != 0 then we can have [x,y,1], and we just plot some sols of y^2 = x^3 + x + l and normalise these values
'''

import matplotlib.pyplot as plt
import numpy as np
from tqdm  import tqdm

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z)

l = 1
def curve_plot(l):
    t0 = np.linspace(-5,5,1001)
    t = t0[np.power(t0,3) - t0 + l >= 0]
    y0 = np.sqrt(np.power(t,3) - t + l)
    x = np.hstack((t[::-1],t))
    y = np.hstack((y0[::-1],-y0))

    z = np.ones(len(x))

    v = np.stack((x, y, z), axis=1)
    norm = np.linalg.norm(v, axis=1)
    unit = v / norm[:, None]
    return unit

unit = curve_plot(1)
ax.plot(unit[:,0], unit[:,1], unit[:,2])

ax.set_aspect('equal')

plt.show()