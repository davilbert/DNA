import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
a=int(input())
mpl.rcParams['legend.fontsize'] = 10

theta = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
z = np.linspace(-2, 2, 1000)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
cs = 1/r

theta1 = np.linspace(4 * np.pi, -4 * np.pi, 1000)
z1 = np.linspace(2, -2, 1000)
r1 = z1**2 + 1
x1 = -r1 * np.sin(theta1)
y1 =- r1 * np.cos(theta1)
cs1 = 1/r1

colorsMap='jet'
cm = plt.get_cmap(colorsMap)
cNorm = mpl.colors.Normalize(vmin=min(cs)) #, vmax=max(cs))
scalarMap = cmx.ScalarMappable(norm=cNorm) #, cmap=cm)

fig = plt.figure()
scalarMap.set_array(cs)
fig1 = plt.figure()
scalarMap.set_array(cs1)


if(a==1):
    for i in range(-2,0):
        z = np.linspace(-2, 0, 1000)
        theta = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
        p = z**2 + 1
        x = p * np.sin(theta)
        y = p * np.cos(theta)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, c='pink', marker='_', s=1)
    for i in range(1,3):
        z = np.linspace(-2, 0, 1000)
        theta = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
        p = z**2 + 1
        x = p * np.sin(theta)
        y = p * np.cos(theta)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, c='red', marker='_', s=1)
else:
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='green', marker='_', s=1)




if(a==1):
    for i in range(-2,0):
        z1 = np.linspace(-2, 0, 1000)
        theta1 = np.linspace(4 * np.pi, -4 * np.pi, 1000)
        p1 = z1**2 + 1
        x1 = p1 * np.sin(theta1)
        y1 = p1 * np.cos(theta1)
        #ax = fig1.add_subplot(111, projection='3d')
        ax.scatter(x1, y1, z1, c='pink', marker='_', s=1)
    for i in range(1,3):
        z1 = np.linspace(-2, 0, 1000)
        theta1 = np.linspace(4 * np.pi, -4 * np.pi, 1000)
        p1 = z1**2 + 1
        x1 = p1 * np.sin(theta1)
        y1 = p1 * np.cos(theta1)
        #ax = fig1.add_subplot(111, projection='3d')
        ax.scatter(x1, y1, z1, c='red', marker='_', s=1)
else:
    #ax = fig1.add_subplot(111, projection='3d')
    ax.scatter(x1, y1, z1, c='green', marker='_', s=1)




#plt.colorbar(scalarMap)
#ax = fig1.gca(111,projection='3d')
ax.scatter(x1, y1, z1, c='blue', marker='_', s=1)
#plt.colorbar(scalarMap)
plt.show()
