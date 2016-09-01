#!/usr/bin/python
import sys
import numpy as np
from matplotlib import pyplot as plt
import re
##############survive
n=sys.argv[1]
result=[]
s =open(n).read()
l=re.findall('survive:(\d+)',s)
result=[int(n) for n in l]
result2=[]
n_old=-1
for n in result:
    if n<n_old:
        result2.append(n_old)
    n_old=n
data=result2
n=20
smoothed = np.convolve(data, np.ones(n)/n)[n:-n]
plt.plot(smoothed)

###################loss
#n=sys.argv[1]
#loss=[]
#for s in open(n):
#    l=re.findall('loss:(.+)',s)
#    if len(l)>0:
#        loss.append(int(l[0]))
# 
#   
#
#plt.plot(result2)
plt.show()
