#script for simulating parallel parking probability according to the 538 Riddler Express from 2020_10_09
#https://fivethirtyeight.com/features/can-you-parallel-park-your-car/

import random as rand

parked = 0
not_parked = 0

i = 0

def CanPark(spaces):
    '''takes an array of spaces and determines if you can park in that arrangement or free spots (i.e. last spaces open or two contiguous open spots)

    array of 1's and 0's -> bool'''

    if spaces[5] == 0 or '0, 0' in str(spaces):
        return True

    else:
        return False

while i < 1000000:
    parking_spaces = [0,0,0,0,0,0]
    
    while sum(parking_spaces) < 4:
        parking_spaces[rand.randint(0,5)] = 1

    if CanPark(parking_spaces):
        parked += 1
        i += 1
        continue

    else:
        not_parked += 1
        i += 1
        continue

print("Parked " + str(parked) + " out of " + str(i) + " times.")
prob = (parked/i)*100

print("This equates to a " + str(prob) + "% chance of parking.")

    


            
