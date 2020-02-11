#!/usr/bin/python
import sys
import numpy as np

data = np.genfromtxt(sys.argv[1], delimiter=',')
outliers=[]
def detect_outliers(data):
    
    threshold=3
    mean = np.mean(data)
    std =np.std(data)
    c=0
    for i in data:
        z_score= (i - mean)/std 
        if np.abs(z_score) > threshold:
            outliers.append(c)
        c=c+1
    return outliers
out_pt=detect_outliers(data)
print(len(out_pt))
data_o = np.delete(data, out_pt, axis=None)
np.savetxt('data_o.csv', data_o, delimiter=',',fmt='%d')