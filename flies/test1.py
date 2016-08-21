import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import math
import mpl_toolkits.mplot3d.axes3d as p3
from numpy import numpyzdetz


fig = plt.figure()
ax = p3.Axes3D(fig)
# fig, ax = plt.subplots()


px = 0
py = 0
pz = 0


point = ax.scatter([px], [py], [pz], 'ro')
# point = ax.plot([px], [py], [pz], 'ro')[0]
# import ipdb; ipdb.set_trace()

def update_point(perlin_x):
    point.set_xdata(math.sin(perlin_x))
    point.set_ydata(math.sin(perlin_x))
    print(point.get_xdata())
    print(point.get_ydata())
    # import ipdb; ipdb.set_trace()
    # point.set_zdata(math.sin(perlin_x) + 2)
    return point,




ani = animation.FuncAnimation(fig, update_point, 25, interval=50, fargs=(point))



plt.show()
