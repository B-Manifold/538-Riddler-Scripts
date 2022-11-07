#Script for simulating mexican bingo as a solution for the 538 Riddler Classic from 2022_10_21
#https://fivethirtyeight.com/features/can-you-make-the-fidget-spinner-go-backwards/

import numpy as np
import random as rand

def make_board(nums):
    '''returns a 4x4 array of random numbers from 1 to 54

    list -> array'''
    board = []
    selection = rand.sample(nums, k = 16)
    board.append(selection[slice(0,4)])
    board.append(selection[slice(4,8)])
    board.append(selection[slice(8,12)])
    board.append(selection[slice(12,16)])
    return np.asarray(board)

def make1000boards(nums):
    '''returns a list of 1000 simulated boards

    list -> list of arrays'''
    boards = []
    for i in range(0,1000):
        boards.append(make_board(nums))
    return boards

def is_winner(board):
    '''tells if board is a winning board given the winning pattern conditions

    array -> bool'''

    #first check if there are even 4 hits in the board
    if len(np.unique(board)) > 13:
        return False
    
    #check the winning conditions

    #corners
    
    if board[0,0] == board[0,3] == board[3,0] == board[3,3] ==0:
        return True

    #rows
    zeros = np.zeros(4,dtype=int)
    
    if np.array_equal(board[:,0],zeros) or\
         np.array_equal(board[:,1],zeros) or\
         np.array_equal(board[:,2],zeros) or\
         np.array_equal(board[:,3],zeros):
        return True

    #columns
    if np.array_equal(board[0,:],zeros) or\
         np.array_equal(board[1,:],zeros) or\
         np.array_equal(board[2,:],zeros) or\
         np.array_equal(board[3,:],zeros):
        return True

    #squares
    zeros = np.zeros((2,2),dtype=int)
    if np.array_equal(board[0:2,0:2],zeros) or\
         np.array_equal(board[1:3,0:2],zeros) or\
         np.array_equal(board[2:,0:2],zeros) or\
         np.array_equal(board[0:2,1:3],zeros) or\
         np.array_equal(board[1:3,1:3],zeros) or\
         np.array_equal(board[2:,1:3],zeros) or\
         np.array_equal(board[0:2,2:],zeros) or\
         np.array_equal(board[1:3,2:],zeros) or\
         np.array_equal(board[2:,2:],zeros):
        return True

    #4 or more hits, but not in a winning pattern
    else:
        return False

def mark_hits(list_of_boards,number):
    '''takes a board and a number (or list of numbers), replaces any instances of that number on the board with 0

    array -> array'''
    new_boards = []
    if type(number) == list:
        for board in list_of_boards:
            for num in number:
                board[board == num] = 0
            new_boards.append(board)
        return new_boards
    else: #number is a single int
        for board in list_of_boards:
            board[board == number] = 0
            new_boards.append(board)
        return new_boards
        

def play_bingo(nums):
    '''simulates one game of mexican bingo (54 pictures, 4x4 boards) with 1000 boards playing returns True if a single board wins on the 5th number. False in all other cases

    list of ints -> bool'''
    boards = make1000boards(nums)
    called_numbers = rand.sample(nums, k = 5)
    #mark boards for the first 4 numbers called
    boards = mark_hits(boards,called_numbers[0:4])
    #See if there are any winning boards after the 4th number is called
    for board in boards:
        if is_winner(board):
            return False
        else:
            continue

    #mark boards for the 5th number called
    boards = mark_hits(boards,called_numbers[4])
    winners = []
    for board in boards:
        if sum(winners) > 1:
            return False
        winners.append(is_winner(board))
##        if is_winner(board):
##            print(board)
##            input("Press enter to continue")
    if sum(winners) == 1:
        return True
    else: #winners == 0, someone wins after the 5th number
        return False

###Simulation Script###
nums = list(np.linspace(1,54,54,dtype=int))
outcomes = []
simuls = 10000
for i in range(0,simuls):
    if not i%50:
        print(str(i) + ' completed simulations out of ' + str(simuls))
    outcomes.append(play_bingo(nums))
percent = 100*(sum(outcomes)/len(outcomes))
print('Out of ' + str(simuls) + ' simulations, ' + str(percent) + '% of the games were won by exactly 1 person on the 5th number.')
print('\nSCRIPT DONE')
