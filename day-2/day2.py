

import numpy as np

def load_data():
    with open('day2.input', 'r') as f:
        data = f.readlines()
    colors={"red":0,"green":1,"blue":2}
    games={}
    for i in range(len(data)):
        after_game = data[i].split(":")
        number_trials = after_game[-1].split(";")
        trial_matrix = [0,0,0]
        trial_matrix = np.array(trial_matrix)
        for trial in number_trials:
            results = trial.split(",")
            result_matrix= [0,0,0]
            for result in results:
                result= result.strip()
                cubes = result.split(" ")
                result_matrix[colors[cubes[1]]] = int(cubes[0])
            result_matrix = np.array(result_matrix)
            trial_matrix = np.max([trial_matrix,result_matrix],axis=0)
        games[i+1]=trial_matrix
                
    return games

games = load_data()
sum_ids = 0
for i in range(1,len(games)+1):
    if games[i][0]<=12 and games[i][1]<=13 and games[i][2]<=14:
        sum_ids+=i 
print(sum_ids)