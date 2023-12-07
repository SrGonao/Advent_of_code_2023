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

sorted_maps = {}
for key in maps:
    sorted_maps[key] = sorted(maps[key], key=lambda x: x[1])




def check_destination_seeds(value,distance, map):
    max_value = value+distance
    original_distance = distance
    min_value = value
    possibilities = []
    #print(len(map))
    distances = []
    for i in range(len(map)):
        destination = map[i][0]
        source = map[i][1]
        distance = map[i][2]
        max_source = source + distance
        minimum = max(min_value,source)
        maximum = min(max_value,max_source)
        if minimum < maximum:
            difference = minimum - source
            position = destination + difference
            print(source,position,difference,minimum,maximum)

            possibilities.append(position)
            distances.append(maximum-minimum)
        if i == 0:
            if value < source :
                
                possibilities.append(value)
                if value + distance < source:
                    distances.append(distance)
                else:
                    distances.append(source-value)
        if i == len(map)-1:
            if max_value > max_source:
                print("here")

                possibilities.append(max(value,max_source))
                distances.append(max_value - max(value,max_source))

    if len(possibilities) == 0:
        possibilities.append(value)
        distances.append(original_distance)
    return possibilities, distances

keys = list(sorted_maps.keys())
positions=[]
#seeds = [82,1]
for i in range(0,len(seeds),2):
    position = seeds[i]
    distance = seeds[i+1]
    first_possibilities,first_distances = check_destination_seeds(position,distance,sorted_maps[keys[0]]) 
    print(first_possibilities,first_distances)
    print("seed:",i)
    for j in range(1,len(keys)):
        print("map:",j)
        possibilities = []
        distances = []
        for k in range(len(first_possibilities)):
            p,d = check_destination_seeds(first_possibilities[k],first_distances[k],sorted_maps[keys[j]])
            print(p,d)
            for i in range(len(p)):
                if p[i] not in possibilities:
                    possibilities.append(p[i])
                    distances.append(d[i])
             
        first_possibilities = possibilities
        first_distances = distances
    positions.append(min(first_possibilities))
    
print(min(positions))
        
