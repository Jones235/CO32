#Author: Michael Jones
#Date: 28/11/18

#Fourier transform function for a 1 dimendional signal
#Inputs: Real part of input function, imaginary part, N (where function inputs range from x=-N to x=N)
#Outputs: Real, imaginary and total amplitudes of transform

import math
import numpy as np

def ft1 (If, Rf, N):

    #Initialise arrays for transformed signal. R, I and T refer to real, imaginary and total amplitudes, respectively.
    
    RF = np.zeros(2*N)
    IF = np.zeros(2*N)

    #Perform fourier transform using the expression given in the lab script.
    
    for u in range (-N, N):

        sum_r = 0 #sum to give real part of transformed signal
        sum_i = 0 #sum to give imaginary part

        for x in range (-N, N):

            sum_r += Rf[x+N]*math.cos(-math.pi*x*u/N) - If[x+N]*math.sin(-math.pi*x*u/N)
            sum_i += Rf[x+N]*math.sin(-math.pi*x*u/N) - If[x+N]*math.cos(-math.pi*x*u/N)

        RF[u+N] = sum_r/(2*N)
        IF[u+N] = sum_i/(2*N)

    TF = np.sqrt(np.square(RF) + np.square(IF))

    return IF, RF, TF
