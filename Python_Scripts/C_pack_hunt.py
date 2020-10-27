# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:19:05 2020

@author: serva
"""
import numpy as np
import scipy.stats
from scipy.stats import binom
# the two give the same results 


# Initialize parameters
X_MAX = 30 # Maximum value of X = gut capacity
X_CRITICAL = 3 # Value of X (gut content) at which death occurs
X_INC = 1 # Increment in state variable
INDEX_MAX = 1 + (X_MAX - X_CRITICAL)/X_INC # Maximum index value
N_PATCH = 4  # Number of patches = packs
COST = 6 # Daily food requirement

Y = 11.25 # Size of single prey
k = [0,1,2,3] # Number of kills
Pi = [0.15, 0.31, 0.33, 0.33]  # Probability of single kill for pack size
benefit = np.zeros([N_PATCH, len(k)])  
p_benefit = np.zeros([N_PATCH, len(k)])  # Probability of finding food in the 3 patches

scipy.stats.binom.pmf(k, 3, Pi[1])
for pack_size in range(1, 5) : # Iterate over pack sizes
    p_benefit[pack_size,] = scipy.stats.binom.pmf(k, 3, Pi[pack_size]) # Calculate binomial probabilities using function dbinom
    benefit[pack_size, 2:4] = Y * k[2:4] / pack_size # Calculate benefits = amount per individual

HORIZON = 31  # Number of time steps

f_vectors = np.zeros([INDEX_MAX, 2]) """pb float"""
f_vectors[1:INDEX_MAX, 1] = 1
fxtt = np.zeros([HORIZON, INDEX_MAX])
mat_best_patch = np.zeros([HORIZON, INDEX_MAX])
FxtT <- matrix(0,Horizon,Max.Index) # F(x,t,T)
Best.Patch <- matrix(0,Horizon,Max.Index) # Best patch number
CHOICES <- matrix(0,Horizon,Max.Index) #



def fitness():
    Max.Index = 1 + (W)