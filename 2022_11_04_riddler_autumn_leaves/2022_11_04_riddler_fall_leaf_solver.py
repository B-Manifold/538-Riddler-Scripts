#Simulates the changing of the leaves, saves multichannel tif stacks of a siulated forrest over the 90 days of autumn, prints the peak autumn colors day
#Maximum fall colors can be found by looking at the Z plot of mean value in ImageJ
#Problem described in 538 Riddler Classic: https://fivethirtyeight.com/features/when-will-the-fall-colors-peak/
import numpy as np
from PIL import Image
import tifffile as tif
import imageio
import random as rand
from tkinter.filedialog import askdirectory


def generate_times():
    '''generates an tuple of random times (days) for a tree to change to its autumn colors, then drop its leaves

    None -> tuple'''
    turn = rand.randint(0,89)
    drop = rand.randint(turn,89)
    return (turn,drop)

def generate_tree_time_array(x_y_trees):
    '''Generates an array representing the change and drop times for a simulated forrest of trees that is x_y_trees by x_y_trees big

    int -> nd array of shape [xy_trees,xy_trees,2]'''
    turn_drop = np.zeros((x_y_trees,x_y_trees,2),dtype='uint8')
    for i in range(x_y_trees):
        for j in range(x_y_trees):
            time = generate_times()
            turn_drop[i,j,0] = time[0]
            turn_drop[i,j,1] = time[1]
    return turn_drop

def change_trees(trees_array,tree_times,time):
    '''takes a forrest simulation, the change/drop times for the trees in the forrest, and the current time (day) and returns 'picture' of the forrest after changing the appropriate trees in the fromn the last day given the day
    sets tree value to 1 if in autumn coloring, is otherwise 0

    ndarray[trees,trees,n_days], ndarray[trees,trees,2], int -> nd array[trees,trees,1]'''
    indices_to_change = np.transpose((tree_times[:,:,0] == time).nonzero())
    indices_to_drop = np.transpose((tree_times[:,:,1] == time).nonzero())
    try:
        new_trees = np.copy(trees_array[:,:,-1])
    except IndexError:
        new_trees = np.copy(trees_array[:,:])
    for cindex in indices_to_change:
        new_trees[tuple(cindex)] = 1
    for dindex in indices_to_drop:
        new_trees[tuple(dindex)] = 0
    return new_trees

def run_season(xy_trees):
    '''Creates a simulation of a "forest" of xy_tress by xy_trees over the 90 days of autumn (includes day 0 before autumn equinox)

    int -> ndarray of shape [xy_trees, xytrees, 91]'''
    trees = np.zeros((xy_trees,xy_trees),dtype='uint8')
    tree_times = generate_tree_time_array(xy_trees)
    for day in range(90):
        trees = np.dstack((trees,change_trees(trees,tree_times,day)))
    return trees
#Script for simulating and saving "forests" of various sizes
path = askdirectory(title='Select Folder to which to save Tiffs') # shows dialog box and return the path
trees10_anyl = run_season(10)
#print(trees10_anyl.shape)
imageio.mimwrite((path+'trees10_anyl.tif'),trees10_anyl.transpose())
trees100_anyl = run_season(100)
#print(trees100_anyl.shape)
tif.imsave((path+'trees100_anyl.tif'),trees100_anyl.transpose())
trees500_anyl = run_season(500)
#print(trees500_anyl.shape)
tif.imsave((path+'trees500_anyl.tif'),trees500_anyl.transpose())

colors = []
for day in range((trees500_anyl.shape)[2]):
    colors.append(np.sum((trees500_anyl[:,:,day])))
print(str(np.amax(colors)))
print('Peak autumn occurs on Day ' + str(np.argmax(colors)))
print("SCRIPT COMPLETE, ENJOY AUTUMN")
