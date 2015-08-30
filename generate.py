"""Generate a set of n files each containing a sample data set for the
   simulated annealing programs.
"""

import numpy as np
import pandas as pd

n = 10  # number of data sets to Generate
M = 25  # number of plots per dataset
N = 5   # number of attributes per plot

arr = map(lambda row:map(lambda x:x*2, row), np.random.random((M,N)));
print arr

df = pd.DataFrame(arr)
csv = df.to_csv(path_or_buf=None, sep=',', header=False, index=False)
print csv
# np.savetxt("foo.csv", arr, delimiter=",", fmt="%1.5f")
