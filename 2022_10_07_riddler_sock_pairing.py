#Script for simulating the sock pairing Riddler from 2022_10_07
#https://fivethirtyeight.com/features/can-you-fold-all-your-socks/

import random as rand
import math

def sock_pairing_sim(num_pairs,num_spaces):
    '''simulates one round of pairing a given number of sock pairs given a number of available interim spaces as described in the problem. Returns bool if pairing is successful

    int,int -> bool'''
    basket = []
    chair = []

    for pair in range(0,num_pairs):
        basket.append(str(pair))
        basket.append(str(pair))

    while len(basket) != 0 and len(chair) <= num_spaces:
        pulled_sock = rand.choice(basket)
        basket.remove(pulled_sock)
        if pulled_sock in chair:
            chair.remove(pulled_sock)
            continue
        elif len(chair) < num_spaces:
            chair.append(pulled_sock)
            continue
        else: #chair is full!
            break
##    print('\n')
##    print('Last sock pulled: ' + str(pulled_sock))
##    print('basket = ' + str(basket))
##    print('chair = ' + str(chair))
    if len(chair) == 0 and len(basket) == 0:
##        print('SUCCESS')
        return True
    else:
##        print('FAILED')
        return False
def sock_sim(num_pairs,num_spaces,sims):
    '''runs sims number of sock pairing sims for num_pairs of socks with num_spaces of interim spaces. Returns percent of successful simulations for the given parameters

    int,int,int -> float'''
    num_sims = sims
    successes = 0
    fails = 0
    for sims in range(0,num_sims):
        if sock_pairing_sim(num_pairs,num_spaces):
            successes += 1
        else: #failed to put all socks away
            fails += 1
    return round(((successes/num_sims)*100),4)

#Script params, simulating multiple sock and space conditions
max_sock_pairs = 30
max_spaces = 30
sims_per_cond = 5000
conditions = {}
#Simulation of the various conditions
for num_pairs in range(1, max_sock_pairs + 1):
    print(str(num_pairs) + '/' + str(max_sock_pairs))
    for num_spaces in range(1, num_pairs +1):
        condition = str(num_pairs) + ',' + str(num_spaces)
        conditions[condition] = sock_sim(num_pairs,num_spaces,sims_per_cond)
print(conditions)
