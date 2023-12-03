import numpy as np


def check_letter(line,indx):
    i=indx
    value=""
    dictionary={"o":["one"],"t":["two","three"],"f":["four","five"],"s":["six","seven"],"e":["eight"],"n":["nine"]}
    values = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    possibilities = dictionary[line[i]]
    for possibility in possibilities:
        if i+len(possibility) < len(line):
            if line[i:i+len(possibility)] == possibility:
                value+=values[possibility]
                return value
    return value
                
def check_letter_backwards(line,idx):
    i=idx
    value=""
    dictionary={"e":["one","three","five","nine"],"o":["two"],"r":["four"],"x":["six"],"n":["seven"],"t":["eight"]}
    values = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    possibilities = dictionary[line[i]]
    for possibility in possibilities:
        if i-len(possibility) >= 0:
            if line[i-len(possibility)+1:i+1] == possibility:
                value+=values[possibility]
                return value
    return value

input = np.loadtxt("day1.input", dtype=str)
calibrations = []
numbers="0123456789"
numbers_string=["one","two","three","four","five","six","seven","eight","nine"]
for line in input:
    value = ""
    for i in range(len(line)):
        if line[i] in numbers:
            value+=line[i]
         #   print(i,line[i])
            break
        if line[i] in ["o","t","f","s","e","n"]:
            test=check_letter(line,i)
            if test != "":
                value+=test
                break


    for i in range(len(line)-1,0,-1):
        #print(i,line[-i])
        if line[i] in numbers:
            value+=line[i]
            #print(i,line[i])
            break
        if line[i] in ["e","o","r","x","n","t"]:
            test=check_letter_backwards(line,i)
            if test != "":
                value+=test
                break
    
    if len(value) == 1:
        value += value
    calibrations.append(int(value))
sum = np.sum(calibrations)
print(sum)