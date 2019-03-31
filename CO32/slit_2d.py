#Author: Michael Jones
#Date: 03/12/18

#Fourier transform for 2D slit(s)

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ft_2d_func import ft2

#input matrices have dimension 2NX2M
N = 25
M = 25
N_list = [i for i in range (-N,N)]
M_list = [i for i in range (-M,M)]
n, m = np.meshgrid(N_list, M_list)  # create an array of coordinates

#set imaginary part of each source equal to zero
If = np.zeros((2*N,2*M))

#set real part of each function
#Rf1 is a cross shaped source at the centre of the lattice
#Rf2 is a square shaped source

Rf1 = np.zeros((2*N,2*M))
Rf2 = np.zeros((2*N,2*M))

for i in ((N-1,N-1), (N-1,N), (N-1,N-2), (N,N-1), (N-2,N-1)):
    Rf1[i] = 1

for i in ((N,N), (N,N-1), (N-1,N), (N-1,N-1)):
    Rf2[i] = 1

#perform fourier transform
IF1, RF1, TF1 = ft2(If, Rf1, N, M)
IF2, RF2, TF2 = ft2(If, Rf2, N, M)

#plot the real and total amplitudes of the transformed signals
fig0 = plt.figure(0)
ax0 = fig0.add_subplot(111, projection="3d")
ax0.plot_surface(n, m, TF1, cmap="Blues_r")
plt.title("Total transformed signal of cross source")

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection="3d")
ax2.plot_surface(n, m, TF2, cmap="Blues_r")
plt.title("Total transformed signal of square source")

plt.figure(1)
plt.imshow(Rf1, cmap="Greys_r")
plt.title("Cross source")

plt.figure(3)
plt.imshow(Rf2, cmap="Greys_r")
plt.title("Square source")

plt.show()
