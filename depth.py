import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

curve = 'Voltage'
mean_length = 200
step = 10

Z = np.array([])

print("Gathering data")
for i in range(1, 101):
    df = pd.read_csv(f'./data/DIODE ({i}).csv', header=[0, 1])

    data = df[curve].values.T[0]
    data = np.convolve(data, np.ones(mean_length)/mean_length, mode='valid')[::step]

    if i == 1:
        Z = data
    else:
        Z = np.vstack((Z, data))

print("Saving depth")
np.savetxt('depth.dat', Z, delimiter=' ', fmt='%07.4f')

print("Creating plot")
x = np.array(range(Z.shape[0]))
y = np.array(range(Z.shape[1]))

X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` data to be 2D

print("Draw 3d")
hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')
ha.plot_surface(X, Y, Z.T)

plt.show()

print("Draw grayscale")
gs = plt.figure()
plt.imshow(Z, cmap="gray")

plt.show()
