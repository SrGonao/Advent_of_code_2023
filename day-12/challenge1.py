from functools import cache
def spring_arrangements():
    broken_springs = []
    unknown_springs = []
    with open("day-12/input", "r") as f:
        for line in f.readlines():
            separated = line.split(" ")
            
            unknown_springs.append(separated[0]*5)
            numbers = separated[1][:-1].split(",")
            
            cleaned_numbers = []
            for number in numbers:
                cleaned_numbers.append(int(number))
            broken_springs.append(tuple(cleaned_numbers))
    return broken_springs,unknown_springs
@cache
def unresolved_springs(broken_spring,unknown_spring):

    if not unknown_spring:
        if not broken_spring:
            return 1
        else:
            return 0
    if not broken_spring:
        if "#" in unknown_spring:
            return 0
        else:
            return 1

    result = 0
    if unknown_spring[0] in ".?":
        result += unresolved_springs(broken_spring,unknown_spring[1:])
    if unknown_spring[0] in "?#":
        if (broken_spring[0] <= len(unknown_spring)
        and "." not in unknown_spring[:broken_spring[0]]
        and (broken_spring[0] == len(unknown_spring) or unknown_spring[broken_spring[0]] != "#")
        ):
            result += unresolved_springs(broken_spring[1:],unknown_spring[broken_spring[0]+1:])
      
            
    #print(broken_spring,unknown_spring,result)
    return result


broken_springs,unknown_springs = spring_arrangements()
sum = 0
for i in range(len(broken_springs)):
    sum += unresolved_springs(broken_springs[i],unknown_springs[i])
print(sum)