import numpy as np
def load_input(file_path):
    history = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            digits = line.split(' ')
            history.append(digits)
    return history


def find_lasts(values):
    lasts = [values[-1]]
    differences = np.diff(values)
    count_zeros = np.sum(differences == 0)
    while count_zeros != len(differences) :
        lasts.append(differences[-1])
        
        differences = np.diff(differences)
        count_zeros = np.sum(differences == 0)
        
    return lasts
        


history = load_input('day-9/input')



nexts = []
for i in range(len(history)):
    values = np.array(history[i], dtype=int)
    lasts = find_lasts(values)
    nexts.append(np.sum(lasts))

print(np.sum(nexts))
