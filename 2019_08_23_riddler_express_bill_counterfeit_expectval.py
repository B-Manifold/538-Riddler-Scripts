##Script to help solve 538 Riddler Express from 2019_08_23. Problem description link:
##https://fivethirtyeight.com/features/can-you-fool-the-bank-with-your-counterfeit-bills/
import operator as op
from functools import reduce
import math
import random

def ncr(n, r):
    '''calculates nCr for n and r

    int, int -> float'''
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer/denom

def ptri(row):
    '''returns the nuumbers from the row-th row of pascals triangle as a list

    int -> list of floats'''
    result = []
    i = row
    while i >= 0:
        result.append(ncr(row, i))
        i = i - 1
    return result

def prob_fakes(fakes):
    '''calculates probability weights of each associated outcome up to 100 total bills (i.e. 5 bills drawn)

    int -> list of floats'''
    total_bills = 25 + fakes
    sampled_bills = math.ceil(total_bills*0.05)
    if fakes == 0:
        prob_list = [1,0,0]
        return prob_list
    if sampled_bills == 2:
        denom = total_bills * (total_bills - 1)
        rr = (25*24)/denom
        rf = (2*25*fakes)/denom
        ff = (fakes * (fakes-1))/denom
        prob_list = [rr,rf,ff]
        return prob_list
    elif sampled_bills == 3:
        denom = total_bills * (total_bills - 1) * (total_bills - 2)
        rrr = (25*24*23)/denom
        rrf = (3*25*24*fakes)/denom
        rff = (3*25*fakes*(fakes-1))/denom
        fff = (fakes*(fakes-1)*(fakes-2))/denom
        prob_list = [rrr,rrf,rff,fff]
        return prob_list
    elif sampled_bills == 4:
        denom = total_bills * (total_bills - 1) * (total_bills - 2) * (total_bills - 3)
        rrrr = (25*24*23*22)/denom
        rrrf = (4*25*24*23*fakes)/denom
        rrff = (6*25*24*fakes*(fakes-1))/denom
        rfff = (4*25*fakes*(fakes-1)*(fakes-2))/denom
        ffff = (fakes*(fakes-1)*(fakes-2)*(fakes-3))/denom
        prob_list = [rrrr,rrrf,rrff,rfff,ffff]
        return prob_list
    elif sampled_bills == 5:
        denom = total_bills * (total_bills - 1) * (total_bills - 2) * (total_bills - 3) * (total_bills - 4)
        rrrrr = (25*24*23*22*21)/denom
        rrrrf = (5*25*24*23*22*fakes)/denom
        rrrff = (10*25*24*23*fakes*(fakes-1))/denom
        rrfff = (10*25*24*fakes*(fakes-1)*(fakes-2))/denom
        rffff = (5*25*fakes*(fakes-1)*(fakes-2)*(fakes-3))/denom
        fffff = (fakes*(fakes-1)*(fakes-2)*(fakes-3)*(fakes-4))/denom
        prob_list = [rrrrr,rrrrf,rrrff,rrfff,rffff,fffff]
        return prob_list
    elif sampled_bills == 6:
        denom = total_bills * (total_bills - 1) * (total_bills - 2) * (total_bills - 3) * (total_bills - 4) * (total_bills - 5)
        rrrrrr = (25*24*23*22*21*20)/denom
        rrrrrf = (6*25*24*23*22*21*fakes)/denom
        rrrrff = (15*25*24*23*22*fakes*(fakes-1))/denom
        rrrfff = (20*25*24*23*fakes*(fakes-1)*(fakes-2))/denom
        rrffff = (15*25*24*fakes*(fakes-1)*(fakes-2)*(fakes-3))/denom
        rfffff = (6*25*fakes*(fakes-1)*(fakes-2)*(fakes-3)*(fakes-4))/denom
        ffffff = (fakes*(fakes-1)*(fakes-2)*(fakes-3)*(fakes-4)*(fakes-6))/denom
        prob_list = [rrrrrr,rrrrrf,rrrrff,rrrfff,rrffff,rfffff,ffffff]
        return prob_list
    elif sampled_bills == 7:
        denom = total_bills * (total_bills - 1) * (total_bills - 2) * (total_bills - 3) * (total_bills - 4) * (total_bills - 5) * (total_bills - 6)
        rrrrrrr = (25*24*23*22*21*20*19)/denom
        rrrrrrf = (7*25*24*23*22*21*20*fakes)/denom
        rrrrrff = (21*25*24*23*22*21*fakes*(fakes-1))/denom
        rrrrfff = (35*25*24*23*22*fakes*(fakes-1)*(fakes-2))/denom
        rrrffff = (35*25*24*23*fakes*(fakes-1)*(fakes-2)*(fakes-3))/denom
        rrfffff = (21*25*24*fakes*(fakes-1)*(fakes-2)*(fakes-3)*(fakes-4))/denom
        rffffff = (7*25*fakes*(fakes-1)*(fakes-2)*(fakes-3)*(fakes-4)*(fakes-6))/denom
        fffffff = (fakes*(fakes-1)*(fakes-2)*(fakes-3)*(fakes-4)*(fakes-6)*(fakes-7))/denom
        prob_list = [rrrrrrr,rrrrrrf,rrrrrff,rrrrfff,rrrffff,rrfffff,rffffff,fffffff]
        return prob_list
def expected_depo(fakes):
    '''calculates expected deposit value given fakes number of fake $100 bills mixed with 25 real $100 bills

    int -> float with 2 decimal places'''
    probs = prob_fakes(fakes)
    i = 0
    money = 0
    max_fakes = math.ceil((25+fakes)*0.05)
    while i <= max_fakes:
        expect = (0.75**(i)) * probs[i] * (2500 + (fakes * 100))
        money = money + expect
        i = i + 1
    money = round(money, 2)
    return money

#Script to determin optimal fake bill number to add. Prints expected deposit values for # of fakes 0-115
fakes = 0
while fakes < 116:
    output = []
    output.append(fakes)
    output.append(expected_depo(fakes))
    print(output)
    fakes = fakes + 1
