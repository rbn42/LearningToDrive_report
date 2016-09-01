#!/usr/bin/python
import re
from matplotlib import pyplot as plt
import numpy as np
import sys
data = []
for s in open(sys.argv[1]):
    l = re.findall('dataset size:(.+)', s)
    data += [float(i) for i in l]
n = 10
smoothed = np.convolve(data, np.ones(n) / n)[n:-n]
#smoothed = smoothed.clip(-1, 1)
plt.plot(smoothed)
plt.show()
