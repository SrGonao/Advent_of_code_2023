times =  [38677673]
distances = [234102711571236]

def max_distance(time):
    
    traveled = []
    for i in range(time):
        velocity = i
        distance = (time-i)*velocity
        traveled.append(distance)
    return traveled

ways = []
for i,t in enumerate(times):
    traveled = max_distance(t)
    way=0
    for t in traveled:
        if t > distances[i]:
            way+=1
    ways.append(way)

mult = 1
for w in ways:
    mult *= w

print(mult)