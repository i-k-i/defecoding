import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

#  make data
xs, ys, zs = np.random.normal(0, 10, 1000), np.random.normal(0, 10, 1000), np.random.normal(0, 10, 1000)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D acceleration vector distribution')

#  make color change over time
cm = plt.get_cmap('Set2')
colors = np.linspace(0, 1, len(xs))
my_colors = cm(colors)

ax.scatter(0, 0, 0, 'o', c='r')  # mark origin
ax.scatter(xs, ys, zs, 'o', alpha=1, c=colors, edgecolors='None',
            cmap=cm)

plt.show()
