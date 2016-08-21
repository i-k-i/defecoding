"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
# import ipdb; ipdb.set_trace()

line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, 10, interval=25)
# ani = animation.FuncAnimation(fig, animate, 50, init_func=init, interval=25, blit=True)
plt.show()
