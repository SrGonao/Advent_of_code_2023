def load_data():
    with open('day-4/input', 'r') as f:
        data = f.readlines()
    winning_numbers = []
    scratch_numbers = []
    for i in range(len(data)):
        data[i] = data[i][:-1]
        numbers = data[i].split(":")[1:]
        print(numbers)
        numbers = numbers[0].split("|")
        wn = numbers[0].split(" ")
        sn = numbers[1].split(" ")
        #remove empty strings
        wn = [int(x) for x in wn if x]
        sn = [int(x) for x in sn if x]
        winning_numbers.append(wn)
        scratch_numbers.append(sn)
    return winning_numbers, scratch_numbers

def check_win(winning_numbers, scratch_numbers):
    total_values=[]
    counts = []
    for i in range(len(winning_numbers)):
        value = 0
        count = 0
        for j in range(len(winning_numbers[i])):
            if winning_numbers[i][j] in scratch_numbers[i]:
                count += 1
                if value == 0:
                    value = 1
                    
                else:
                    value = value*2
        total_values.append(value)
        counts.append(count)
    return total_values, counts


winning_numbers, scratch_numbers = load_data()

total_values,count = check_win(winning_numbers, scratch_numbers)

scratches={}
for i in range(len(count)):
    if i in scratches:
        scratches[i]+=1
    else:
        scratches[i]=1
    for j in range(i+1,i+count[i]):
        if j in scratches:
            scratches[j]+=scratches[i]
        else:
            scratches[j]=scratches[i]



print(sum(scratches.values()))