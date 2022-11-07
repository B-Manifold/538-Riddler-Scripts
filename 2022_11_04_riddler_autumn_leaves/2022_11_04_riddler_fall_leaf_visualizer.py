#Simulates the changing of the leaves, saves multichannel tif stacks of a simulated forrest over the 90 days of autumn, uses pretty values for Autumn_Leaves.lut Look Up Table in ImageJ
#See other script for analytical version to find the peak day, this one is jsut to create a cool animated gif to submit
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
    randomly assigns pixel values of 101-255 if in autumn color, 0-10 if leaves have dropped

    ndarray[trees,trees,n_days], ndarray[trees,trees,2], int -> nd array[trees,trees,1]'''
    indices_to_change = np.transpose((tree_times[:,:,0] == time).nonzero())
    indices_to_drop = np.transpose((tree_times[:,:,1] == time).nonzero())
    try:
        new_trees = np.copy(trees_array[:,:,-1])
    except IndexError:
        new_trees = np.copy(trees_array[:,:])
    for cindex in indices_to_change:
        new_trees[tuple(cindex)] = rand.randint(101,255)
    for dindex in indices_to_drop:
        new_trees[tuple(dindex)] = rand.randint(0,10)
    return new_trees

def run_season(xy_trees):
    '''Creates a simulation of a "forest" of xy_tress by xy_trees over the 90 days of autumn (includes day 0 before autumn equinox)

    int -> ndarray of shape [xy_trees, xytrees, 91]'''
    trees = ((89*np.random.rand(xy_trees,xy_trees))+11).astype('uint8') #assigning pixel values 11-100 for trees with leaves pre autumn colors (green in LUT)
    tree_times = generate_tree_time_array(xy_trees)
##    print(np.amax(trees_init))
##    print(np.amin(trees_init))
    for day in range(90):
##      print(trees.shape)
        trees = np.dstack((trees,change_trees(trees,tree_times,day)))
##        print(trees.shape)
##        print(np.amax(trees[:,:,-1]))
##        print(np.amin(trees[:,:,-1]))
    return trees
path = askdirectory(title='Select Folder to which to save Tiffs')
trees10 = run_season(10)
print(trees10.shape)
imageio.mimwrite((path+'trees10.tif'),trees10.transpose())
trees100 = run_season(100)
print(trees100.shape)
tif.imsave((path+'trees100.tif'),trees100.transpose())
trees500 = run_season(500)
print(trees500.shape)
tif.imsave((path+'trees500.tif'),trees500.transpose())
