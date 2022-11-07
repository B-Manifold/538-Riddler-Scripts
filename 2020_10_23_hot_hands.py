##Script for simulating the hot hands Ridler Express from 2020_10_23
#https://fivethirtyeight.com/features/can-you-feed-the-hot-hand/

import random as rand

def shot():
    '''creates a list of 3 bools representing whether a shot was made

    none -> list of bools'''
    shots = []
    i = 0
    while i < 3:
        shots.append(bool(rand.randint(0,1)))
        i += 1
    return shots

def trial_picker(trial_list):
    '''tells if a trial list contains shot that was preceeded by a made shot

    list of bools -> bool'''
    ttt = [True,True,True]
    ttf = [True,True,False]
    tft = [True,False, True]
    ftt = [False,True,True]
    ftf = [False,True,False]
    tff = [True,False,False]
    possible_trials = [ttt,ttf,tft,ftt,ftf,tff]
    
    if trial_list in possible_trials:
        return True
    else:
        return False
        

def shot_picker(trial_list):
    '''takes a list of 3 shot trials returns a if a shot (that was preceeded by a made shot) is made

    list of bools -> bool'''
    ttt = [True,True,True]
    ttf = [True,True,False]
    tft = [True,False, True]
    ftt = [False,True,True]
    ftf = [False,True,False]
    tff = [True,False,False]
    
    if trial_list == ttt:
        return 1

    elif trial_list == ttf:
        return rand.randint(0,1)

    elif trial_list == tft:
        return 0

    elif trial_list == ftt:
        return 1

    elif trial_list == ftf:
        return 0

    elif trial_list == tff:
        return 0

i = 0

shots_made = 0
shots_missed = 0

while i < 10000:
    j = 0
    trial_list = []
    while j < 50:
        current_trial = shot()
        if trial_picker(current_trial):
            trial_list.append(current_trial)
            j += 1
            continue
        else:
            j += 1
            continue
    current_trial = rand.choice(trial_list)
    current_shot = shot_picker(current_trial)
    if current_shot:
        shots_made += 1
        i += 1
        continue
    else:
        shots_missed += 1
        i += 1
        continue

total_shots = shots_made + shots_missed
print("Hot Hand probability = " + str((shots_made/total_shots)*100))
