#script for cracking 2-digit 7-seg safe combo for riddler express 2022/09/30
#https://fivethirtyeight.com/features/can-you-crack-the-safe/

#useful functions
def encode(num):
    '''Takes an integer 0 to 9 representing a digit and creates a list of binaries representing the 7-segment digital read out pattern for that digit

    int -> list of ints (0 for off, 1 for on)'''
    if num == 0:
        return [1,1,1,1,1,1,0]
    elif num == 1:
        return [0,1,1,0,0,0,0]
    elif num == 2:
        return [1,1,0,1,1,0,1]
    elif num == 3:
        return [1,1,1,1,0,0,1]
    elif num == 4:
        return [0,1,1,0,0,1,1]
    elif num == 5:
        return [1,0,1,1,0,1,1]
    elif num == 6:
        return [1,0,1,1,1,1,1]
    elif num == 7:
        return [1,1,1,0,0,0,0]
    elif num == 8:
        return [1,1,1,1,1,1,1]
    elif num == 9:
        return [1,1,1,1,0,1,1]

def add_codes(code_a, code_b):
    '''takes 2 7-segment digital codes and 'adds' them at each segment to create the 'fade' pattern for that combination of digits

    list of 7 ints, list of 7 ints -> list of 7 ints'''
    added = []
    for seg in range(7):
        added.append(code_a[seg]+code_b[seg])
    return added

#script for generating the possible unique 2-digit combinations and their resultant "fade" patterns in the 7-segment digital read-out
digits = [0,1,2,3,4,5,6,7,8,9]
combos = {}

for dig in digits:
    dig_dummy = dig
    while dig_dummy in digits:
        key = str(dig) + str(dig_dummy)
        combos[key] = add_codes(encode(dig),encode(dig_dummy))
        dig_dummy += 1
print("there are " + str(len(combos)) + " unique combinations of 2-digits.")

#checking all the combinations for any two unique combinationations that would result in the same "fade" pattern
for combo in combos:
    for combo_check in combos:
        if combos[combo] == combos[combo_check] and combo != combo_check:
            print(str(combo) + ' and ' + str(combo_check) + ' will have the same fade pattern.')
