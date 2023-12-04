import numpy as np





def load_data():
    
    with open('day-3/day3.input', 'r') as f:
        data = f.readlines()
   
    for i in range(len(data)):
        data[i] = data[i][:-1]
    return data    



def find_signs(data):
    unique=[]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in ["1","2","3","4","5","6","7","8","9","0","."] and data[i][j] not in unique:
                unique.append(data[i][j])
    return unique


def find_coordinates(data,signs):
    coordinates=[]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in signs:
                coordinates.append([i,j])
    return coordinates

def find_next(x,y,data):
    x0=x
    y0=y
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    number = ""
    while data[y][x] in numbers:
        number+=data[y][x]
        x+=1
        #print(y,x)
        if x>=len(data[y])-1:
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
                #j =-1, i=-1 -> 0
                #j =-1, i=1 -> 1
                #j =1, i=-1 -> 2
                #j =1, i=1 -> 3
                found[(i+1)//2+(j+1)] = True
                number = find_next(x+j,y+i,data)      
                if number != "":
                    if number not in neighbors[-30:]:
                     neighbors.append(number)          
                
    if not found[0] and not found[1]:
        if data[y][x-1] in numbers:
            number = find_next(x-1,y,data)
            if number != "":
                    if number not in neighbors[-30:]:
                     neighbors.append(number) 
                
    if not found[2] and not found[3]:
        if data[y][x+1] in numbers:
            number = find_next(x+1,y,data)
            if number != "":
                    if number not in neighbors[-30:]:
                     neighbors.append(number) 
            
    if not found[0] and not found[2]:
        if data[y-1][x] in numbers:
            number = find_next(x,y-1,data)
            if number != "":
                    if number not in neighbors[-30:]:
                     neighbors.append(number) 
            
    if not found[1] and not found[3]:
        if data[y+1][x] in numbers:
            number = find_next(x,y+1,data)
            if number != "":
                    if number not in neighbors[-30:]:
                     neighbors.append(number) 
            

    #print(neighbors)
    return neighbors

def find_numbers(data,coordinates):
    numbers=[]
    
    for i in range(len(coordinates)):
        #check all neighbors
        neighbors_list = neighbors(coordinates[i],data)
        if len(neighbors_list)>0:
            for n in neighbors_list:
                numbers.append(n)
    return numbers






data = load_data()
signs = find_signs(data)
coordinates = find_coordinates(data,signs)
numbers = find_numbers(data,coordinates)
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(sum(numbers))


for i in [-1,1]:
    for j in [-1,1]:
        print(i,j)
        print((i+1)//2+(j+1))