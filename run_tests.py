import random
import sys
import math
import re

import npuzzle

def random_move(node,k):

    nodecopy = node[:]
    zero1 = node.index('-')
    nodecopy[zero1] = 1
    zero2 = nodecopy.index('-') 
    nodecopy = node[:]

    n = zero1 if random.randint(0,1) else zero2

    row = n//k

    do = random.randint(1,4)

    if (do==1) and not (n==k*row):
          num = node[n-1]
          node[n] = num
          node[n-1] = '-'

    if (do==2) and not (n==k*(row+1)-1):
          num = node[n+1]
          node[n] = num
          node[n+1] = '-'

    if (do==3) and not row==0:
          num = node[n-k]
          node[n] = num
          node[n-k] = '-'


    if (do==4) and not row==k-1:
          num = node[n+k]
          node[n] = num
          node[n+k] = '-'

    


def generate_goal(node,k,n_moves):
  nodecopy = node[:]
  for i in range(n_moves):
    random_move(nodecopy,k)
  return nodecopy

def generate_start(k):
    tiles = [i for i in range(1,k**2-1)] + ['-','-']
    random.shuffle(tiles)

    return(tiles)


#Generating test results

def compare(k,results,num_moves=30):

  start = generate_start(k)
  goal = generate_goal(start,k,num_moves)

  num_nodes_misplaced = npuzzle.npuzzle(k,start,goal,"misplaced")[0]
  num_nodes_manhattan = npuzzle.npuzzle(k,start,goal,"manhattan")[0]

  results.append([num_nodes_misplaced,num_nodes_manhattan])


def do_tests():
#Initializing empty array
    results = []

    for i in range(50):
      compare(5,results)

    for i in range(30):
      compare(7,results)

    for i in range(20):
      compare(10,results,num_moves=25)

    for i in range(6):
      compare(12,results,num_moves=20)

    for i in range(5):
      compare(15,results,num_moves=20)

    compare(20,results,num_moves=20)

    return results




