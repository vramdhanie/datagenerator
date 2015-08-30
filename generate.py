"""Generate a set of n files each containing a sample data set for the
   simulated annealing programs.
"""

import numpy as np

n = 10  # number of data sets to Generate
M = 25  # number of plots per dataset
N = 5   # number of attributes per plot

arr = map(lambda row:map(lambda x:x*2, row), np.random.random((M,N)));
print arr

np.savetxt("foo.csv", arr, delimiter=",", fmt="%1.5f")
