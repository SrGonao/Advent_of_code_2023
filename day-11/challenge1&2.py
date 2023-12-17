
def get_galaxy_map():
    galaxy_map = []
    with open("day-11/input", "r") as f:
        for y,line in enumerate(f.readlines()):
            for x,char in enumerate(line):
                if char == "#":
                    galaxy_map.append((y,x))
    return galaxy_map

def expand_galaxy_map(galaxy_map,factor):
    max_x = max([pair[1] for pair in galaxy_map])
    max_y = max([pair[0] for pair in galaxy_map])
    not_in_x = [x for x in range(max_x) if x not in [pair[1] for pair in galaxy_map]]
    not_in_y = [y for y in range(max_y) if y not in [pair[0] for pair in galaxy_map]]
    expanded_map = []
   
    for pair in galaxy_map:
        y,x = pair
        new_y,new_x = (y,x)
        
        for u_x in not_in_x:
            if x > u_x:
                new_x += factor
        for u_y in not_in_y:
            if y > u_y:
                new_y += factor
        
        expanded_map.append((new_y,new_x))
    return expanded_map

def find_galaxy_pairs(galaxy_map):
    pairs = []
    
    for i,pair in enumerate(galaxy_map):
        for j,pair2 in enumerate(galaxy_map):
            if j > i:
                pairs.append((pair,pair2,i+1,j+1))
    return pairs

def shortest_path(galaxy_pairs):
    paths = []
    for pair in galaxy_pairs:
        y1,x1 = pair[0]
        y2,x2 = pair[1]
        paths.append(abs(y1-y2) + abs(x1-x2))
    return paths





galaxy_map = get_galaxy_map()
expanded = expand_galaxy_map(galaxy_map,1)
galaxy_pairs = find_galaxy_pairs(expanded)
paths = shortest_path(galaxy_pairs)
print(sum(paths))


galaxy_map = get_galaxy_map()
expanded = expand_galaxy_map(galaxy_map,999999)
galaxy_pairs = find_galaxy_pairs(expanded)
paths = shortest_path(galaxy_pairs)
print(sum(paths))