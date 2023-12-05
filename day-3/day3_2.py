import numpy as np





def load_data():
    
    with open('day-3/day3.input', 'r') as f:
        data = f.readlines()
   
    for i in range(len(data)):
        data[i] = data[i][:-1]
    return data    


def find_coordinates(data,signs):
    coordinates=[]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in signs:
                coordinates.append([i,j])
    return coordinates

def find_next(y,x,data):
    x0=x
    y0=y
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    number = ""
    while data[y][x] in numbers:
        number+=data[y][x]
        x+=1
        #print(y,x)
        if x>=len(data[y]):
            break
    reverse_number = ""
    x=x0
    y=y0
    while data[y][x] in numbers:
        reverse_number+=data[y][x]
        x-=1
        if x<0:
            break
    reverse_number = reverse_number[::-1]
    number = reverse_number[:-1]+number
    return number

def neighbors(coordinate,data):
    y=coordinate[0]
    x=coordinate[1]
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    neighbors=[]
    found=[False,False,False,False]
    
    for i in [-1,1]:
        for j in [-1,1]:
            if data[y+i][x+j] in numbers:
                #i= -1 , j =-1, -> 0
                #i= 1  , j =-1  -> 1
                #i= -1 , j =1,  -> 2
                #i= 1  , j =1,  -> 3
                found[(i+1)//2+(j+1)] = True
                number = find_next(y+i,x+j,data)      
                if number != "":
                    if number not in neighbors[-10:]:
                     neighbors.append(number)          
                
    if data[y][x-1] in numbers:
        number = find_next(y,x-1,data)
        if number != "":
                if number not in neighbors[-10:]:
                    neighbors.append(number) 
                
    if data[y][x+1] in numbers:
        number = find_next(y,x+1,data)
        if number != "":
                if number not in neighbors[-10:]:
                    neighbors.append(number) 
            
    if not found[0] and not found[2]:
        if data[y-1][x] in numbers:
            number = find_next(y-1,x,data)
            if number != "":
                    if number not in neighbors[-10:]:
                     neighbors.append(number) 
            
    if not found[1] and not found[3]:
        if data[y+1][x] in numbers:
            number = find_next(y+1,x,data)
            if number != "":
                    if number not in neighbors[-10:]:
                     neighbors.append(number) 
    #print(neighbors)
    return neighbors

def find_numbers(data,coordinates):
    numbers=[]
    
    for i in range(len(coordinates)):
        #check all neighbors
        neighbors_list = neighbors(coordinates[i],data)
        if len(neighbors_list)==2:
            numbers.append(neighbors_list)
    return numbers




data = load_data()
signs = ["*"]

all_numbers=[]
coordinates = find_coordinates(data,signs)
numbers = find_numbers(data,coordinates)
mult = []
for i in range(len(numbers)):
    mult.append(int(numbers[i][0])*int(numbers[i][1]))
print(sum(mult))

