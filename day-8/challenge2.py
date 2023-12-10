import math
def load_input(input_file):
    maps = {}
    line_nr = 0
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if line_nr == 0:
                intructions=line
                line_nr += 1
            else:
                if line != "":
                    line = line.split(" = ")
                    directions = line[1].split(", ")
                    maps[line[0]] = [directions[0][1:],directions[1][:-1]]
    return intructions, maps

intructions, maps = load_input("day-8/input")

starts = []
ends = []
for key in maps.keys():
    last_letter = key[-1]
    if last_letter == "A":
        starts.append(key)
    elif last_letter == "Z":
        ends.append(key)

#while not finished:
idx = {"L":0,"R":1}
number_steps=0
paths=[]

for start in starts:
    number_steps = 0
    finished = False

    while not finished:
        
        position = number_steps % len(intructions)
        
        next = maps[start][idx[intructions[position]]]
        start = next
        number_steps += 1
        if start in ends:
            finished = True
            print("finished")
            paths.append(number_steps)
    
print(math.lcm(*paths))



