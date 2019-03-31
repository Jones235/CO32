#Author: Michael Jones
#Date: 03/12/18

#Fourier transform function for a 2 dimensional signal
#Inputs: Real part of input function, imaginary part, N (where -N<x<N), M (where -M<y<M)
#Output: Real, imaginary and total amplitudes of transform

import math
import numpy as np

def ft2 (If, Rf, N, M):

    #Initalise arrays for transformed signal. R, I and T refer to real, imaginary and total amplitudes, respectively.

    RF = np.zeros((2*N,2*M))
    IF = np.zeros((2*N,2*M))

    #Perform transform using the expression derived in my lab book.

    for u in range (-N, N):

        for v in range (-M, M):

            sum_r = 0 #sum to give real part of transformed signal
            sum_i = 0 #sum to give imaginary part

            for x in range (-N, N):

                for y in range (-M, M):

                    sum_r += Rf[x+N,y+M]*math.cos(math.pi*(x*u/N + y*v/M))  +  If[x+N,y+M]*math.sin(math.pi*(x*u/N + y*v/M))
                    sum_i += If[x+N,y+M]*math.cos(math.pi*(x*u/N + y*v/M))  -  Rf[x+N,y+M]*math.sin(math.pi*(x*u/N + y*v/M))

            RF[u+N,v+M] = sum_r/(4*N*M)
            IF[u+N,v+M] = sum_i/(4*N*M)

    TF = np.sqrt(np.square(RF) + np.square(IF))

    return IF, RF, TF

            
