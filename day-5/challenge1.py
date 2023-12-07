

maps = {}
with open('day-5/input', 'r') as f:
        data = f.readlines()
        current = ""
        for i in range(len(data)):
            if "seeds:" in data[i]:
                values = data[i].split(":")[1:]
                values = values[0].split(" ")
                seeds = [int(x) for x in values if x]
            if "map" in data[i]:
                current = data[i].split("map:")[0]
            if current != "" and "map" not in data[i]:
                if current not in maps:
                    maps[current] = []
                data[i] = data[i][:-1]
                values = data[i].split(" ")
                if len(values) > 1:
                 maps[current].append([int(x) for x in values if x])


def check_destination(value, map):
    for i in range(len(map)):
        destination = map[i][0]
        source = map[i][1]
        distance = map[i][2]
        if value > source and value < source + distance:
            difference = value - source
            position = destination + difference
            return position
    return value

positions=[]
for seed in seeds:
    position = seed
    for key in maps:
        position = check_destination(position, maps[key])
    print(seed, position)
    positions.append(position)

print(min(positions))
        
