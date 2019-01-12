#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import timeit 
import sys
import numpy as np
from copy import deepcopy

# ABDecision will return the action that maximizes the MinValue of the first successors of the given state
def ABDecision(state, depth,  player):
    
    value = -float('inf')
    best_move = ''  
    next_state = []
    for [child, move] in successor(state,player):
        
        val = MinValue(child,depth-1, -float('inf'), float('inf'))        
        if val > value:
            value = val
            best_move = move
            next_state = child
    return best_move, next_state #,end1

# will return the maximum of Beta values calculated by MinValue,
# establishing a lower bound and pruning Beta values lower than the lower bound 
#while updating the lower bound if a larger value of Beta is encountered.   
def MaxValue(state, depth, alpha, beta):
    temp,Goal = isGoal(state,opposition_player)
    if Goal==1:
        return temp
    if depth == 0:
        return evaluation(state)
    for [child,move] in successor(state,current_player):
        evl = MinValue(child, depth-1, alpha, beta)
        alpha = max(evl,alpha)
        if beta <= alpha:
            return alpha
    return alpha

# will return the minimum of Alpha values calculated by MaxValue,
# establishing an upper bound and pruning Alpha values larger than the upper bound 
#while updating the upper bound if a smaller value of Alpha is encountered.
def MinValue(state, depth, alpha, beta):
    temp,Goal = isGoal(state,current_player)
    if Goal==1:
        return temp
    if depth == 0:
        return evaluation(state)
    for [child,move] in successor(state,opposition_player):
        evl = MaxValue(child, depth-1, alpha, beta)
        beta = min(evl,beta)
        if alpha >= beta:
            return beta
    return beta
    
def successor(state,player):
    c=0
    for i in range(0,N+3):
        for j in range(0,N):
            if state[i][j] == player:
                c+=1
                
    successors = []
    if c<(N*(N+3)/2):
        for j in range(0,N):# filling up the bottomost row, if empty.
            if state[N+3-1][j] == '.':
                tempSt = deepcopy(state)
                tempSt[N+3-1][j] = player
                move = j+1
                successors.append([tempSt,move])
    if c<(N*(N+3)/2):        
        for i in range(0,N+2):# filling up the rest of the rows, if the position is available
            for j in range(0,N):
                if state[i][j] == '.' and state[i+1][j] != '.':
                    tempSt = deepcopy(state)
                    tempSt[i][j] = player
                    move = j+1
                    successors.append([tempSt,move])
                  
    for i in range(0,N):#rotating the columns
        list1 = []
        if state[N+3-1][i] != '.':
            tempSt = deepcopy(state)  
            m = -1
            for j in range(0,N+3):                
                if tempSt[j][i] == '.':
                    m = j    
                list1.append(tempSt[j][i])
            if m==-1:
                list1 = [list1[-1]] + list1[0:N+2] 
            else:
                list1 = list1[0:m+1] + [list1[N+2]] + list1[m+1:N+2]
            for k in range(0,N+3):
                tempSt[k][i]=list1[k]
            move = -(i + 1)
            successors.append([tempSt,move])
    
    return successors
               
def evaluation(state):    
    #for rows, our heuristic assigns an evaluation of 2^(number of our pebbles in a row). This will assign higher value to moves which increase
    # the number of our pebbles in the row which already has the maximum count of our pebbles.
    temp_value = 0
    evalue = 0
    for i in range(0,N):
        row_count = 0
        for j in range(0,N):
            if state[i][j]==current_player:
                row_count += 1
        temp_value = 2**row_count
        evalue += temp_value    
    
    #for columns, our heuristic assigns an evaluation of 2^(number of our pebbles in a column). This will assign higher value to moves which increase
    # the number of our pebbles in the column which already has the maximum count of our pebbles.
    for j in range(0,N):
        col_count = 0
        for i in range(0,N):
            if state[i][j]==current_player:
                col_count += 1
        temp_value = 2**col_count
        evalue += temp_value 
    
    #for diagonals, our heuristic assigns an evaluation of 2^(number of our pebbles in a diagonal). This will assign higher value to moves which increase
    # the number of our pebbles in the diagonal which already has the maximum count of our pebbles.   
    diag_count1 = 0
    diag_count2 = 0
    for i in range(0,N):
        if state[i][i]==current_player:
            diag_count1 += 1
        if state[i][N-i-1]==current_player:
            diag_count2 += 1
    temp_value = 2**diag_count1 + 2**diag_count2
    evalue += temp_value
    
    #the above evaluation functions for row, column and diagonals, consider only the top N rows.
    
    #The above evaluators will not be useful for an empty, or a sparcely filled state. The evaluaters below are for the bottom 3 rows.
    #A sparsely filled state in itself will most likely not tell much about the the best step, and it is imperative that the state
    #contains pebbles in top N rows to get a better judgement of the next move. The below evaluator counts the number of both pebbles 
    #and adds them to the evaluation function          
    count=0
    for i in range(N,N+3):
        for j in range(0,N):
            if (state[i][j] == current_player) or (state[i][j] == opposition_player):
                count+=1
    evalue += count
    
    #More the number of our pebbles in the bottom row, the more it is beneficial for us as after rotation they will be on the top rows. The benefit increases as we move down the rows
    #i.e. if the bottommost should be given more value for the number of our pebbles it has. In the below evaluator the
    #(N+3) row will be valued (count of our pebbles) * 3 , N+2 will be valued (count of our pebbles)* 2 and N+1 will be valued (count of our pebbles) * 1
    for i in range(N,N+3):
        b3_count = 0
        for j in range(0,N):
            if state[i][j]==current_player:
                b3_count += 1
        temp_value = b3_count*(i-N+1)
        evalue += temp_value 

    return evalue

# in the goal state we check if any state is a goal state for the player and the opponent and return infinity for the player and negative infinity for the opponent.                    
def isGoal(state,player):
    
    for i in range(0,N):
        check1 = 1
        for j in range(0,N-1):
            if (state[i][j]!=state[i][j+1]) or state[i][j]=='.':
                check1 = 0
                break
        if check1 == 1:
            if player == current_player:
                return float('inf'),1
            else:
                return -float('inf'),1
            
    for j in range(0,N):
        check2 = 1
        for i in range(0,N-1):
            if state[i][j]!=state[i+1][j] or state[i][j]=='.':
                check2 = 0
                break
        if check2 == 1:
            if player == current_player:
                return float('inf'),1
            else:
                return -float('inf'),1
            
    check3 = 1        
    for i in range(0,N-1):
        if state[i][i] != state[i+1][i+1] or state[i][i]=='.':
            check3 = 0
            break
        if state[i][N-i-1] != state[i+1][N-i-2]or state[i][N-i-1]=='.':
            check3 = 0
            break
    if check3 == 1:
        if player == current_player:
            return float('inf'),1
        else:
            return -float('inf'),1
        
    return 0,0
    
start = timeit.default_timer()             
N = int(sys.argv[1])
current_player = sys.argv[2]
if current_player == 'x':
    opposition_player = 'o'
else:
    opposition_player = 'x'
ini_state = list(sys.argv[3])
initial_state = []
for i in range(0,N*(N+3),N):
    initial_state.append(ini_state[i:i+N])
time = float(sys.argv[4])
#We are applying Iterative Deepening with step size 1. 
i=1
while i>0:    
    mov,n_state =  ABDecision(initial_state, i,  current_player)
    #time_2 = timeit.default_timer()-start
    new_state = []
    for i in range(0,N+3):
        for j in range(0,N):
            new_state.append(n_state[i][j])
    new_state = ''.join(new_state)
    print('Id recommend the mov \n')
    print mov, ""+new_state 
    i+=1
