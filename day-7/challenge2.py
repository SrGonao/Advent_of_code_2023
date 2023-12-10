import numpy as np 
def read_data(path):
    hands,bids = [],[]
    with open(path,"r") as f:
        for line in f:
            line = line.strip()
            h,b = line.split(" ")
            hands.append(h)
            bids.append(b)
    return hands,bids


def card_to_number(card):
    if card == "J":
        return 0
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    elif card == "T":
        return 10
    else:
        return int(card)

def hand_to_numbers(hand):
    numbers = []
    for card in hand:
        numbers.append(card_to_number(card))
    return numbers
    
def type_of_hand(hand):
    sorted_hand = sorted(hand)
    counts = {}
    for card in sorted_hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    if 0 in counts:
        if counts[0]==1:
            if 4 in counts.values():
                return "5 of a kind"
            elif 3 in counts.values():
                return "4 of a kind"
            elif 2 in counts.values():
                keys = [key for key in counts.keys() if counts[key] == 2]
                if len(keys) == 2:
                    return "full house"
                else:
                    return "3 of a kind"
            elif 1 in counts.values():
                return "1 pair"
        if counts[0]==2:
            if 3 in counts.values():
                return "5 of a kind"
            elif 2 in counts.values():
                keys = [key for key in counts.keys() if counts[key] == 2]
                if len(keys) == 2:
                    return "4 of a kind"
                else:
                    return "3 of a kind"
            elif 1 in counts.values():
                return "3 of a kind"
        if counts[0]==3:
            if 2 in counts.values():
                return "5 of a kind"
            elif 1 in counts.values():
                return "4 of a kind"
        if counts[0]==4:
            if 1 in counts.values():
                return "5 of a kind"
        if counts[0]==5:
            return "5 of a kind"
    type = ""
    if 5 in counts.values():
        type = "5 of a kind"
    elif 4 in counts.values():
        type = "4 of a kind"
    elif 3 in counts.values() and 2 in counts.values():
        type = "full house"
    elif 3 in counts.values():
        type = "3 of a kind"
    elif 2 in counts.values():
        keys = [key for key in counts.keys() if counts[key] == 2]
        if len(keys) == 2:
            type = "2 pairs"
        else:
            type = "1 pair"
    else:
        type = "high card"
    return type
        
def sort_typed_hands(typed_hands):
    value = []
    type_to_value = {"high card":1,"1 pair":2,"2 pairs":3,"3 of a kind":4,"full house":5,"4 of a kind":6,"5 of a kind":7}
    value_to_type = {1:"high card",2:"1 pair",3:"2 pairs",4:"3 of a kind",5:"full house",6:"4 of a kind",7:"5 of a kind"}
    for i in range(len(typed_hands)):
        value.append(type_to_value[typed_hands[i]])
    sorted_hands = []
    for i in range(len(value)):
        sorted_hands.append((value[i],i))
    #print(sorted_hands)
    sorted_hands = sorted(sorted_hands)
   
    for i in range(len(sorted_hands)):
        sorted_hands[i] = (value_to_type[sorted_hands[i][0]],sorted_hands[i][1])
    

    return sorted_hands

def sort_between_types(numbered,indexes):
    #all these cards are tied. The first card breaks the tie, then the second, etc.
    numbers_to_letters = {14:"A",13:"B",12:"C",11:"D",10:"E",9:"F",8:"G",7:"H",6:"I",5:"J",4:"K",3:"L",2:"M",1:"N",0:"O"}
    letter_hands = []
    for i in range(len(numbered)):
        hand = ""
        for j in range(len(numbered[i])):
            hand=hand+numbers_to_letters[numbered[i][j]]
        letter_hands.append([hand,i])

    
    sorting_indx = sorted(letter_hands)
    sorted_hands = []
    for i in range(len(sorting_indx)):
        sorted_hands.append(indexes[sorting_indx[i][1]])

    return sorted_hands



hands,bids = read_data("day-7/input")
numbered_hands = []
for hand in hands:
    numbered_hands.append(hand_to_numbers(hand))

typed_hands = []
for hand in numbered_hands:
    typed_hands.append(type_of_hand(hand))


sorted_hands = sort_typed_hands(typed_hands)

type_of_hands = {}
for i in range(len(sorted_hands)):
    if sorted_hands[i][0] not in type_of_hands:
        type_of_hands[sorted_hands[i][0]] = []
        type_of_hands[sorted_hands[i][0]].append(sorted_hands[i][1])
    else:
        type_of_hands[sorted_hands[i][0]].append(sorted_hands[i][1])
sorted_type_of_hands = {}
for key in type_of_hands:
    input = [numbered_hands[i] for i in type_of_hands[key]]
    indexes = [i for i in type_of_hands[key]]
    sorted_type_of_hands[key] = sort_between_types(input,indexes)

final_order = []
final_hands = []
for key in sorted_type_of_hands:
    # go in reverse order
    for i in range(len(sorted_type_of_hands[key])-1,-1,-1):
        final_order.append(sorted_type_of_hands[key][i])
        final_hands.append([hands[sorted_type_of_hands[key][i]],typed_hands[sorted_type_of_hands[key][i]]])

total_score = 0
for i in range(len(final_order)):
    bet = int(bids[final_order[i]])*(i+1)
    total_score += bet


print(total_score)