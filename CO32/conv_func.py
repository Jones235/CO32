#Author: Michael Jones
#Date: 28/11/18

#Convolution function for two 1 dimensional signals
#Inputs: Input functions (u, v), N (where function inputs range from x=-N to x=N).
#Outputs: Normalised convolved signal (c)

import numpy as np
from ft_func  import ft1

def conv1 (u, v, N):

    c = np.zeros(2*N)

    for X in range (N, 3*N): #only include central region of convolution (which has range(0, 4*N)

        conv_sum = 0

        for i in range (2*N): 

            if X-i in range (2*N): #only include valid indices
                
                conv_sum += u[i] * v[X-i] #compute sum to approximate integral given in lab script

        c[X-N] = conv_sum/(2*N) #divide by 2N to normalise

    return c

