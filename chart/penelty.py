#!/usr/bin/python
import re
from matplotlib import pyplot as plt
import numpy as np
import sys
s=open(sys.argv[1]).read()
l=re.findall('penelty rate:(.+)',s)
l=[float(i) for i in l]
data=l
n=20
smoothed = np.convolve(data, np.ones(n)/n)[n:-n]
smoothed=smoothed.clip(-1,1)
plt.plot(smoothed)
plt.show()
