
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





start = "AAA"
idx = {"L":0,"R":1}
number_steps=0
while start != "ZZZ":
    for intruction in intructions:

        next = maps[start][idx[intruction]]
        start = next
        number_steps += 1
print(start)
print(number_steps)





