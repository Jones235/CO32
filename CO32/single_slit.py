#Author: Michael Jones
#Date: 28/11/18

#Fourier transform for a single slits of varying width and height

import math
import numpy as np
import matplotlib.pyplot as plt
from ft_func import ft1

N = 250 #input values range from x=-N to x=N
N_list = [i for i in range (-N, N)] #list of integers spanning the range of the input

#set imaginary part of each input function equal to 0
If = np.zeros(2*N)

#set real part of each function. Value represents the height of the slit at that point.
#Rf1 is a slit of width=10, height=1, centre=0
#Rf2 is a slit of width=10, height=1, centre=-10
#Rf3 is a slit of width=20, height=1, centre=0
#Rf4 is a slit of width=20, height=0.5, centre=0
#Rf5 is 2 slits of width=20, height=1, centre=-15,+15
#Rf6 is 2 slits of width=20, height=1, centre=-25,+25
#Rf7 is 2 slits of width=40, height=1, centre=-25,+25
#Rf8 is 2 slits of width=40, height=0.5, centre=-25,+25


Rf1, Rf2, Rf3, Rf4, Rf5, Rf6, Rf7, Rf8 = [np.zeros(2*N) for _ in range(8)]


for i in range (N-5,N+5):
    Rf1[i] = 1
for i in range (N-15,N-5):
    Rf2[i] = 1
for i in range (N-10,N+10):
    Rf3[i] = 1
    Rf4[i] = 0.5
for i in range (N-25,N-5):
    Rf5[i] = 1
for i in range(N+5,N+25):
    Rf5[i] = 1
for i in range(N-35,N-15):
    Rf6[i] = 1
for i in range(N+15,N+35):
    Rf6[i] = 1
for i in range(N-45,N-5):
    Rf7[i] = 1
    Rf8[i] = 0.5
for i in range(N+5,N+45):
    Rf7[i] = 1
    Rf8[i] = 0.5


#perform fourier transform
'''
IF1, RF1, TF1 = ft1(If, Rf1, N)
IF2, RF2, TF2 = ft1(If, Rf2, N)
IF3, RF3, TF3 = ft1(If, Rf3, N)
IF4, RF4, TF4 = ft1(If, Rf4, N)
'''
IF5, RF5, TF5 = ft1(If, Rf5, N)
IF6, RF6, TF6 = ft1(If, Rf6, N)
IF7, RF7, TF7 = ft1(If, Rf7, N)
IF8, RF8, TF8 = ft1(If, Rf8, N)


#plot the real and total amplitudes of the transformed signal

'''
plt.figure(0)
plt.plot(N_list, TF1)
plt.plot(N_list, RF1)
plt.title("single slit centered on the origin")

plt.figure(1)
plt.plot(N_list, TF2)
plt.plot(N_list, RF2)
plt.title("single slit centered on x=-10")

plt.figure(2)
plt.plot(N_list, TF3**2)
plt.title("intensity - single slit of double width")

plt.figure(3)
plt.plot(N_list, TF4**2)
plt.title("intensity - single slit of double width and half height")

plt.figure(8)
plt.plot(N_list, TF2**2)
plt.title("intensity single slit at -10")


'''
plt.figure(4)
plt.plot(N_list, RF5, N_list, TF5)
plt.title("double slits centred on +/-15")

plt.figure(8)
plt.plot(N_list, RF5**2)
plt.title("intensity - double slits, centre +/-15")

plt.figure(5)
plt.plot(N_list, RF6, N_list, TF6)
plt.title("double slits centred on +/-25")

plt.figure(9)
plt.plot(N_list, TF6**2)
plt.title("intensity - double slits, centre +/-25")

plt.figure(6)
plt.plot(N_list, RF7, N_list, TF7)
plt.title("double slits of double width centred on +/-25")

plt.figure(10)
plt.plot(N_list, TF7**2)
plt.title("intensity - double slits, double width, centre +/-25")

plt.figure(7)
plt.plot(N_list, RF8, N_list, TF8)
plt.title("double slits of double width and half height centred on +/-25")

plt.figure(11)
plt.plot(N_list, TF8**2)
plt.title("intensity - double slits, double width, half height, centre +/-25")



plt.show()
