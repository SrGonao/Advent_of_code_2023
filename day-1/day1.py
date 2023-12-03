import numpy as np


input = np.loadtxt("day1.input", dtype=str)
calibrations = []
numbers="0123456789"
for line in input:
    value = ""
    for i in range(len(line)):
        if line[i] in numbers:
            value+=line[i]
         #   print(i,line[i])
            break
        
    for i in range(1,len(line)):
        #print(i,line[-i])
        if line[-i] in numbers:
            value+=line[-i]
            #print(i,line[i])
            break
    if len(value) ==1:
        value += value
    calibrations.append(int(value))
sum = np.sum(calibrations)
print(sum)