import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.animation as animation
import random

fig = plt.figure(figsize=(8,6), dpi=150)
x = np.linspace(-2, 4.5, 250)


h=4
a=1
b=3

hlines(y=h, xmin=1, xmax=3, linewidth=1.5)
vlines(x=a, ymin=0, ymax=4, linewidth=1.5)
vlines(x=b, ymin=0, ymax=4, linewidth=1.5)

ylim(-2.5,10.5)
xlim(-2.5,4.5)
grid()

def data_gen():
    i = 0
    while i< 1:
        R1 = random.random()
        R2 = random.random()
        x0 = (b - a)*R1 + a
        y0 = h*R2
        i = i + 1
        yield x0, y0


line, = plot([], [], linestyle='none', marker='o', color='r')

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

xdata, ydata = [], []

def run(data):
    x0,y0 = data
    xdata.append(x0)
    ydata.append(y0)
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=0.5,
    repeat=False)
plt.show()
