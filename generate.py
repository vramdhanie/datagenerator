"""Generate a set of n files each containing a sample data set for the
   simulated annealing programs.
"""

import numpy as np
import pandas as pd

n = 10  # number of data sets to Generate
M = 25  # number of plots per dataset
N = 5   # number of attributes per plot

def generateSet(Plots, Attributes):
    arr = map(lambda row:map(lambda x:x*2, row), np.random.random((Plots, Attributes)))
    df = pd.DataFrame(arr)
    csv = df.to_csv(path_or_buf=None, sep=',', header=False, index=False)
    return csv


f = open('data.txt', 'w')
for i in range(1, n):
    data = ("%d\n%d\n%s\n" % (M, N, generateSet(M, N)))
    f.write(data)
    M += 5
f.close()

# np.savetxt("foo.csv", arr, delimiter=",", fmt="%1.5f")
