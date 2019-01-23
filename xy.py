import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import time

x_curve = 'Voltage'
y_curve = 'Current'
mean_length = 200
step = 10

fig = plt.figure(frameon=False)
fig.set_size_inches(4, 4)
ax = plt.Axes(fig, [0., 0., 1., 1.])
fig.add_axes(ax)

for i in range(1, 101):
    df = pd.read_csv(f'./data/DIODE ({i}).csv', header=[0, 1])

    x = df[x_curve].values.T[0]
    y = df[y_curve].values.T[0]
    x = np.convolve(x, np.ones(mean_length) / mean_length, mode='valid')[::step]
    y = np.convolve(y, np.ones(mean_length) / mean_length, mode='valid')[::step]

    ax.clear()
    ax.plot(x, y, "k")
    ax.set_xlim([0, 12])
    ax.set_ylim([-10, 130])
    ax.set_axis_off()
    fig.savefig(f"./data/DIODE ({i}).pdf", dpi=25, bbox_inches='tight', transparent=True, pad_inches=0)

    #plt.show()

time.sleep(5)

for i in range(1, 101):
    os.system(f'pstoedit -f dxf:"-polyaslines -mm" "./data/DIODE ({i}).pdf" "./data/DIODE ({i}).dxf"')
