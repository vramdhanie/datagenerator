"""Generate a set of n files each containing a sample data set for the
   simulated annealing programs.
"""

import numpy as np
import pandas as pd

n = 10  # number of data sets to Generate
M = 25  # number of plots per dataset
N = 5   # number of attributes per plot
L = 5   # number of land uses

def generateSet(M, N):
    arr = map(lambda row:map(lambda x:x*2, row), np.random.random((M, N)))
    df = pd.DataFrame(arr)
    csv = df.to_csv(path_or_buf=None, sep=',', header=False, index=False)
    return csv


fileName = "data_"

for i in range(0, n):
    f = open(("%s%d.txt"%(fileName, i)), 'w')
    plots = ("%d\n%d\n%s\n" % (M, N, generateSet(M, N)))
    f.write(plots)
    landUses = ("%d\n%d\n%s\n" % (L, N, generateSet(L, N)))
    f.write(landUses)

    for j in range(0, M):
        f.write(("%d,%d\n"%(j,np.random.randint(L))))
    f.close()
    M += 5

# np.savetxt("foo.csv", arr, delimiter=",", fmt="%1.5f")
