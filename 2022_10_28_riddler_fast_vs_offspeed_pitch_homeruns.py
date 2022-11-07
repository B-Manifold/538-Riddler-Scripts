#Script for finding the logical Fastball/Offspeed calls for Pitcher and Batter as described in 538 Riddler Express from 2022_10_28
#https://fivethirtyeight.com/features/can-you-hand-out-all-the-candy/
#distrib (probabiltiy distribution given input pitcher/batter fastball percentages can be saved as a tif and explored as a 3d surface plot in imagj. Forms a Saddle surface
import numpy as np
import random as rand
import math

def pitch_choose(p_fast):

    if rand.randint(1,100) <= p_fast: #pitcher throws a fastball
        return 1
    else: # pitcher throws offspeed
        return 0

def bat_guess(b_fast):
    if rand.randint(1,100) <= b_fast: #batter guesses fastball
        return 1
    else: #batter guesses offspeed
        return 0
        
def play_ball(p_fast,b_fast):
    '''returns True if homerun occurs based on the announced pitcher fastball (p_fast) vs batter fastball (b_fast) probabilities. Returns False for all other cases

    int,int -> bool'''

    pitch = pitch_choose(p_fast)
    bat = bat_guess(b_fast)

    if bat != pitch:
        return False
    if bat == 1:
        if rand.randint(1,5) == 1:
            return True
        else:
            return False
    else:
        if rand.randint(1,2) == 1:
            return True
        else:
            return False

def simulate_games(num_games, p_fast, b_fast):
    '''simulates num_games number of games of single pitch guessing as described by prompt using the announced pitcher fastball (p_fast) vs batter fastball
 (b_fast) probabilities. Returns the percentage of those games that were homeruns

    int, int, int -> float'''
    homer_count = 0
    for i in range(num_games):
        if play_ball(p_fast,b_fast):
            homer_count += 1
    return homer_count/num_games

distrib = np.zeros((101,101),dtype=float)
for p in range(101):
    if p % 10 == 0:
        print(str(p) + '% done simulating')
    for b in range(101):
        distrib[p,b] = simulate_games(5000,p,b)
outcomes = []
probs = []
for row in range(len(distrib[0])):
    outcomes.append(np.argmax(distrib[row,:]))
    probs.append(np.amax(distrib[row,:]))
    #print('Pitch_prob_fast = ' + str(row) + '%\n Batter announces ' + str(np.argmax(distrib[row,:])) + '% guessing fastball with best homerun prob = ' + str(100*np.amax(distrib[row,:])) + '%')

pitch_fcall = outcomes[probs.index(min(probs))]
pitch_ocall = 100-pitch_fcall
bat_fcall = np.argmax(distrib[pitch_fcall,:])
bat_ocall = 100-bat_fcall
hr_prob = round((100*min(probs)),3)
print('Pitcher calls ' + str(pitch_fcall) + '% fast ball and ' + str(pitch_ocall) + '% offspeed')
print('Batter calls ' + str(bat_fcall) + '% fast ball and ' + str(bat_ocall) + '% offspeed')
print('There is a ' + str(hr_prob) + '% probability of a homerun')
