#Script for analytically solving and simulating the modified birthday paradox problem as described in 538 Riddler from 2022_10_13
#https://fivethirtyeight.com/features/can-you-salvage-your-rug/

import random as rand
import math

def nPr(n,r):
    f = math.factorial
    return f(n) // f(n-r)

exp_val = []

#Analytical soltuion for expected value of people in room when cake is eaten
for persons in range(2,366):
    exp_val.append((persons*(persons-1)*nPr(365,(persons-1)))/(365**persons))
print('Analytical expected number of people: ' + str(sum(exp_val)))

def birthday_simulate():
    '''simulates people entering the room and seeing if the last person entering has the same birthday as anyone else in the room. Returns the number of people in the room when this happens

    None -> int'''
    room = []
    last_person = rand.randint(1,365)
    while last_person not in room:
        room.append(last_person)
        last_person = rand.randint(1,365)
    room.append(last_person)
    return len(room)

#Script to simulate 50,000 iterations of people entering the room checking for 2 mutual birthdays
simuls = 50000
people = []
for i in range(0,simuls):
    people.append(birthday_simulate())
avg_people = ((sum(people))/simuls)
print('Simulated expected number of people in room for 2 Birthday condition: ' + str(avg_people))

##EXTRA CREDIT: Three people with mutual birthdays now the sotpping condition for cake
def two_or_fewer(room):
    '''checks the room for mutual birthdays. Returns False if there more than 2 people with the same birthday, otherwise returns true

    list of ints -> bool'''
    if room == []:
        return True
    for person in room:
        if room.count(person)>2:
            return False
    return True

def tri_birthday_simulate():
    '''simulates people entering the room seeing if the last person shares the same birthday with two other people in the room. Returns the number of people in the room when this happens

    None -> int'''
    room = []
    last_person = rand.randint(1,365)
    while two_or_fewer(room):
        room.append(last_person)
        last_person = rand.randint(1,365)
    room.append(last_person)
    return len(room)

#Script to simulate 50,000 iterations of people entering the room checking for 3 mutual birthdays
simuls = 50000
people = []
for i in range(0,simuls):
    people.append(tri_birthday_simulate())
avg_people = ((sum(people))/simuls)
print('Simulated expected number of people in room for 3 Bithday condition: ' + str(avg_people))
