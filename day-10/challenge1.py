

def read_map(file):
    pipe_map = []
    start = None
    simbol_to_number={"|":"up/down","-":"left/right","L":"up/right","J":"up/left","7":"down/left","F":"down/right",".":"filler","S":"start"}
    with open(file, "r") as f:
        for i,line in enumerate(f.readlines()):
            line = line.strip()
            grid_line = []
            for j,char in enumerate(line):
                if char == "S":
                    start = (i, j)
                grid_line.append(simbol_to_number[char])
            pipe_map.append(grid_line)
    return pipe_map,start

def possible_neighbours(pipe_map,position,previous=None):
    y,x = position
    neigbhours = [(y-1,x),(y+1,x),(y,x+1),(y,x-1)]
    ups = ["up/down","up/left","up/right","start"]
    downs = ["up/down","down/left","down/right","start"]
    lefts = ["up/left","down/left","left/right","start"]
    rights = ["up/right","down/right","left/right","start"]
    combinations= {"start":{0:downs,1:ups,2:lefts,3:rights},
                   "up/down":{0:downs,1:ups,2:[],3:[]},
                   "left/right":{0:[],1:[],2:lefts,3:rights},
                   "up/right":{0:downs,1:[],2:lefts,3:[]},
                   "up/left":{0:downs,1:[],2:[],3:rights},
                   "down/left":{0:[],1:ups,2:[],3:rights},
                   "down/right":{0:[],1:ups,2:lefts,3:[]}
                   }
    possible = []
    current = pipe_map[y][x]
    #print(current)
    for neighbour in neigbhours:
        y,x = neighbour
        pipe = pipe_map[y][x]
        #print(pipe,neigbhours.index(neighbour))
        #print(combinations[current])
        
        if pipe in combinations[current][neigbhours.index(neighbour)]:
      #      print(combinations[current][neigbhours.index(neighbour)],current,pipe,position,neighbour)
            if previous is None:
                possible.append(neighbour)
            elif neighbour != previous:
                possible.append(neighbour)

    return possible
        


def make_path(pipe_map,start):
    current = start
    possible = possible_neighbours(pipe_map,current)
    path1 = [start,possible[0]]
    path2 = [start,possible[1]]
    finished = False
    counter = 0
    #while not finished:
    #print(counter,pipe_map[current[0]][current[1]],possible[0])
    while not finished:
        current1 = path1[-1]
        current2 = path2[-1]
        possible1 = possible_neighbours(pipe_map,current1,path1[-2])[0]
        possible2 = possible_neighbours(pipe_map,current2,path2[-2])[0]
        path1.append(possible1)
        path2.append(possible2)
        if possible1 in path2 or possible2 in path1:
            finished = True
        
        counter += 1
     #   print(counter,pipe_map[current[0]][current[1]],possible)
    return path1,path2
    


pipe_map,start = read_map("day-10/input")

path1,path2 = make_path(pipe_map,start)
print(len(path1)-1)


import matplotlib.pyplot as plt
import numpy as np
array1 = np.array(path1)
array2 = np.array(path2)
x = np.arange(0,140,0.5)
y = np.arange(0,140,0.5)
grid = np.ones((len(x),len(y)))
for i in range(len(array1)):
    x1,y1 = array1[i]
    x2,y2 = array2[i]
    grid[x1*2,y1*2] = -1
    grid[x2*2,y2*2] = -1
    if i > 0:
        difx1 = x1 - array1[i-1][0]
        dify1 = y1 - array1[i-1][1]
        difx2 = x2 - array2[i-1][0]
        dify2 = y2 - array2[i-1][1]
        grid[x1*2-difx1,y1*2-dify1] = -1
        grid[x2*2-difx2,y2*2-dify2] = -1


group_grid = np.ones((len(x),len(y)))
groups= {0:[],-1:[]}
positions = {}
last_group = 0
#for y in range(len(grid)):
#    for x in range(len(grid[y])):
for y in range(25,50):
    for x in range(25,50):
        if y ==0 or y == len(grid)-1 or x == 0 or x == len(grid)-1:
            positions[(y,x)] = 0
            group_grid[y,x] = 0
            groups[0].append((y,x))
        
        if group_grid[y,x] == 1 and grid[y,x] != -1:
            positions[(y,x)] = last_group
            group_grid[y,x] = last_group
            groups[last_group] = [(y,x)]
            last_group += 1
        if y < len(grid)-1:
            if grid[y+1,x]!=-1:
                if group_grid[y+1,x] != 1:
                    old_group = group_grid[y,x]
                    new_group = group_grid[y+1,x]
                    for position in groups[old_group]:
                        group_grid[position] = new_group
                        positions[position] = last_group
                    groups[new_group] += groups[old_group]
                    groups[old_group] = []

                else:
                    positions[(y+1,x)] = positions[(y,x)]
                    group_grid[y+1,x] = positions[(y,x)]
                    groups[positions[(y,x)]].append((y+1,x))

            else:
                print("oi")
                positions[(y+1,x)] = -1
                group_grid[y+1,x] = -1
                groups[-1].append((y+1,x))
        if x < len(grid)-1:
            if grid[y,x+1]!=-1:
                if group_grid[y,x+1] != 1:
                    old_group = group_grid[y,x]
                    new_group = group_grid[y,x+1]
                    for position in groups[old_group]:
                        group_grid[position] = new_group
                        positions[position] = last_group
                    groups[new_group] += groups[old_group]
                    groups[old_group] = []

                else:
                    positions[(y,x+1)] = positions[(y,x)]
                    group_grid[y,x+1] = positions[(y,x)]
                    groups[positions[(y,x)]].append((y,x+1))

            else:
                positions[(y,x+1)] = -1
                group_grid[y,x+1] = -1
                groups[-1].append((y,x+1))
            

plt.imshow(group_grid)
plt.ylim(50,25)
plt.xlim(25,50)
plt.figure()
plt.imshow(grid)
plt.ylim(50,25)
plt.xlim(25,50)
            
        
