#script to simulate and analytically solve the "shirt store" problem from 538 riddler express from 2022/09/23
##https://fivethirtyeight.com/features/can-you-buy-the-right-shirt/

import random as rand
import math

#script params
num_customers = 5000
max_shirts = 100

#set up order counts

def nCr(n,r):
    '''returns n choose r calculation for n and r

    int, int -> int'''
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def shirt_analytical(num_shirts):
    exp_returns = []
    exp_orders = []
    for returns in range(0,num_shirts):
        exp_returns.append((nCr(num_shirts-1,returns)/nCr(num_shirts,returns))*(1/(num_shirts-returns))*returns)
        exp_orders.append((nCr(num_shirts-1,returns)/nCr(num_shirts,returns))*(1/(num_shirts-returns))*(returns+1))
    return round(100*(sum(exp_returns)/sum(exp_orders)),2)

#analytical script
print('Analytical Solutions:')
print('number of shirts , percent returns of total orders')
num_shirts = 1
for num_shirts in range(1,max_shirts+1):
    print(str(num_shirts) + ',' + str(shirt_analytical(num_shirts)))


#simulation scripting stuff
def shirt_simulate(num_shirts, num_customers):
    '''simulates the shirt buying process for a given number of shirts in the catalog for a given number of customers

    int, int -> list of 2 ints'''
    orders = {}
    orders["correct"] = 0
    orders["returns"] = 0
    customer_choice = 1
    possible_choices = 1
    cust = 0
    
    for cust in range(0,num_customers):
        customer_choice = rand.randint(1,num_shirts)
        possible_choices = list(range(1,(num_shirts+1)))
        selection = rand.choice(possible_choices)
        while customer_choice != selection:
            orders["returns"] = orders["returns"] + 1
            possible_choices.remove(selection)
            selection = rand.choice(possible_choices)
        orders["correct"] = orders["correct"] + 1

    return [orders["correct"],orders["returns"]]
        


#simulation script
#print('number of shirts,total orders,returns,percent returns')
print('\nSimulation solutions based on ' + str(num_customers) + ' customers per simulation:')
print('number of shirts , percent returns of total orders')
for num_shirts in range(1,max_shirts+1):
    current_orders = shirt_simulate(num_shirts,num_customers)
    total_orders = current_orders[0] + current_orders[1]
    percent_returns =  round(((current_orders[1]/total_orders)*100),2)

    #Verbal Report
##    print("If there are " + str(num_shirts) + " shirts in the catalog, there will be a: \n~" +
##      str(percent_returns) + "% return rate (" + str(current_orders[1]) + "/" +
##      str(total_orders) + " orders)")

    #Data Report [num_shirts, total_orders, returns, percent_returns]
##    print(str(num_shirts) + ',' + str(total_orders) + ',' + str(current_orders[1]) + ',' + str(percent_returns))
    print(str(num_shirts) + ',' + str(percent_returns))
print('done')

