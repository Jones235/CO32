#Author: Michael Jones
#Date: 29/11/18

#Verification of convolution theorem for a single slit.

import math
import numpy as np
import matplotlib.pyplot as plt
from conv_func import conv1
from ft_func import ft1

N = 250 #input values range from x=-N to x=N
N_list = [i for i in range (-N, N)] #list of integers spanning the input values

#Define vector u to represent a single slit of width 20, centred on the origin
u = np.zeros(2*N)
for i in range (N-10, N+10):
    u[i] = 1

#Convolve u with itself
c = conv1 (u, u, N)

#Plot u and the convolution of u
plt.figure(0)
plt.plot(N_list, u)
plt.plot(N_list, c)
plt.title("slit and normalised convolution of slit")

#Transform slit (obtaining real, imaginary and total amplitudes)
IU, RU, TU = ft1(np.zeros(2*N), u, N)

#Transform convolution (obtaining real, imaginary and total amplitudes)
IC, RC, TC = ft1(np.zeros(2*N), c, N)

TU2 = np.square(TU) #square of transform of slit

#plot square of transform of slit
plt.figure(1)
plt.plot(N_list, TU2)
plt.title("square of transform of slit")
plt.figure(2)
#plot transform of convolution
plt.plot(N_list, TC)
plt.title("transform of convolution")
plt.show()

