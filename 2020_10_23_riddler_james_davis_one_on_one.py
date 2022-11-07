#Script for simulating the Lebron James vs Anthony Davis one on one from 538 Riddler classic for 2020_10_23
#https://fivethirtyeight.com/features/can-you-feed-the-hot-hand/
import random as rand

def shot():
    '''simulates a basketball shot with a 50% probability of succeeding, returns whether or not the shot was successful

    None -> bool'''

    return bool(rand.randint(0,1)) #A 50% chance of any shot being made

def lbj_steal(prob):
    '''simulates Lebron stealing stealing the ball from Davis with some changing probability prob, returns whether or not the steal was successful. Prob must be an int [1,1000] representing probability (prob/1000)*100

    int -> bool'''

    stealing = rand.randint(1,1000)

    if stealing <= prob:
        return True #LBJ steals the ball!
    else:
        return False #Davis holds the ball and can go for the shot!


def play_game(davis_has_ball = True, steal_prob = 500):
    '''simulates a game based on whether davis starts with the ball or not and Lebron's stealing probability. Returns whether or not Davis wins the game.

    bool, int(between 1 and 1000) -> bool'''
    shot_made = False
    while not shot_made:
        if davis_has_ball: #Lebron gets a steal chance before Davis can attempt a shot
            if lbj_steal(steal_prob): #LBJ Steals and goes for a shot!
                davis_has_ball = False
                shot_made = shot()
                if not shot_made: #LBJ Misses and Davis gets the rebound!
                    davis_has_ball = True
                    continue
                else: #LBJ drains it!
                    continue
            else: #LBJ fails to steal and Davis goes for the 3!
                shot_made = shot()
                if not shot_made: #Davis misses, but gets his own rebound!
                    davis_has_ball = True
                    continue
                else: #Davis is good on the 3 and wins the game!
                    continue
        else: #Lebron has the ball and goes for the shot!
            shot_made = shot()
            if not shot_made: #Lebron misses and Davis has the rebound!
                davis_has_ball = True
                continue
            else: #Lebron dunks for the win!
                continue
    
    if davis_has_ball: #Davis had the ball when the shot was made (i.e. Davis wins)
        return True
    else: #Lebron had the ball when the shot was made (i.e. James wins)
        return False


lbj_steal_prob = 1 #starting a probability of 0.1%

while lbj_steal_prob <= 1000:
    num_games = 0
    davis_wins = 0
    james_wins = 0
    report = []
    
    #simultating 10,000 games for the given steal probability
    while num_games < 10000:
        davis_has_ball = bool(rand.randint(0,1))
        if play_game(davis_has_ball, lbj_steal_prob):
            davis_wins += 1
            num_games += 1
            continue
        else:
            james_wins += 1
            num_games += 1
            continue

    #building the model report [lbj_steal_prob, davis_win_percentage, james_win_percentage]
    steal_prob = (lbj_steal_prob/1000)*100
    report.append(steal_prob)
    davis_win_prob = (davis_wins/num_games)*100
    report.append(davis_win_prob)
    james_win_prob = (james_wins/num_games)*100
    report.append(james_win_prob)
    print(report) #prints out the report for later analysis
    
    lbj_steal_prob +=1 #inreasing LBJ's stealing probability by 0.1%


