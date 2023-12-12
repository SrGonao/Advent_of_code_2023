import numpy as np
def load_input(file_path):
    history = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            digits = line.split(' ')
            history.append(digits)
    return history


def find_firsts(values):
    firsts = [values[0]]
    differences = np.diff(values)
    count_zeros = np.sum(differences == 0)
    while count_zeros != len(differences) :
        firsts.append(differences[0])
        
        differences = np.diff(differences)
        count_zeros = np.sum(differences == 0)
        
    return firsts
        


history = load_input('day-9/input')



nexts = []
for i in range(len(history)):
    values = np.array(history[i], dtype=int)
    firsts = find_firsts(values)
    total_sum = 0
    for i in range(len(firsts)-1,-1,-1):
        if i % 2 == 0:
            total_sum += firsts[i]
        else:
            total_sum -= firsts[i]
    nexts.append(total_sum)

print(sum(nexts))
