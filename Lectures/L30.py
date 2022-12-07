# recursion
# functions calling themselves as helper funtions
# n! = 1*2*3*...*(n-1)*n

# fact(n) = fact(n-1)*n
# base case: 0! = 1

def fact(n):
    '''return n!'''
    print(n)
    if n == 0:
        return 1
    return fact(n-1)*n

# fact(0) --> 1
# fact(1) --> 1*fact(0)
# fact(2) --> 2*fact(1)
# fact(3) --> 3*fact(2)
# fact(4) --> 4*fact(3)

# verify factorial 0 returns as intended
# since we know what factorial 0 does, we know what factorial 1 does and up and onwards...

# python will limit the number of recursion, eg. fact(4.1) gets limited...

# complexity analysis:
# if n is a float, you can't compute factorial of very large numbers, eg. fact(250.0)
# can't go to more than 170, since fact(171) is inf, so complexity analysis doesn't make sense

# this should work for integers

def is_winning_sum(s): # race to 21
    '''Return True if getting s means you are winning with perfect play, False otherwise'''
    if s == 21:
        return True
    for move in [1, 2]:
        if is_winning_sum(s+move): # if opponent can win with +1 or +2, I lose: such as at 16, opponent can +2 to 18 and will win
            return False
    return True

# is_winning_sum(16): False
# is_winning_sum(17): False
# is_winning_sum(18): True --> opponent +1 or +2 will allow you to be at 19 or 20, and you win
# is_winning_sum(19): False --> opponent can get to 21 by +2
# is_winning_sum(20): False --> opponent can get to 21 by +1
# is_winning_sum(21): True
# 18 wins since 19 and 20 are winning
# 19 is losing since 21 is winning



## GENERAL ALGORITHM

def is_win(state):
    return state == 21

def get_possible_moves(state):
    if state == 21:
        return [1]
    else:
        return [1, 2]

def get_possible_state(state, move):
    return state + move

def is_winning_state(state):
    '''return True if the state means the current player is winning with perfect play'''
    moves = get_possible_moves(state)
    for move in moves:
        possible_state = get_possible_state(state, move)
        if is_winning_state(possible_state):
            return False
            # seeing if opponent move allows them to win
    return True

# nim
# start with a bunch of piles [4, 4, 4]
# take away numbers from one pile only each time
# win if your move leads to [0, 0, 0]

def is_win1(state):
    return sum(state) == 0

def get_possible_moves1(state):
    res = []
    for i in range(1, state[0] + 1):
        res.append([i, 0, 0]) # take i from the first pile, 0 from the others
    for j in range(1, state[1] + 1):
        res.append([0, j, 0])
    for k in range(1, state[2] + 1):
        res.append([0, 0, k])
    return res

def get_possible_state1(state, move):
    new_state = state[:]
    for i in range(len(move)):
        new_state[i] -= move[i]
    return new_state

def is_winning_state1(state): # is winning state stays the same!
    moves = get_possible_moves1(state)
    for move in moves:
        possible_state = get_possible_state1(state, move) # not very efficient, you have to make a new copy of the board for each different state!!!
        if is_winning_state1(possible_state):
            return False
    return True

# Diplomacy