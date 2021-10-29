import random
import sys
import math
import re

def misplaced(config,goal):
    ans = 0
    for i in range(len(config)):
        if config[i]!='-' and config[i]!=goal[i]:
            ans += 1

    return ans

def manhattan(config,goal):
  k = int(math.sqrt(len(config)))
  ans = 0

  for n1 in range(len(config)):
    if config[n1]!='-':
      n2 = goal.index(config[n1])

      r1 = n1//k
      r2 = n2//k
      c1 = n1- k*r1
      c2 = n2 - k*r2

      ans += abs(r1-r2) + abs(c1-c2)
  
  return ans
'''
def h(config,goal):
    return manhattan(config,goal)
    '''

def min_f(queue):
    n = len(queue)
    f = float('INF')
    node_index = -1
    
    for i in range(n):
        if queue[i][1]+queue[i][2] < f:
            node_index = i
            f = queue[i][1]+queue[i][2]

    return node_index 
    

def is_in_queue(queue,config):

    for i in range(len(queue)):
        if queue[i][0] == config:
            return i
    return False

def gen(node,k):

    neighbours=[]
    #node = list(parent)
    nodecopy = node[:]

    zero1 = node.index('-')
    nodecopy[zero1] = 1
    zero2 = nodecopy.index('-')
    
    nodecopy = node[:]

    for n in [zero1,zero2]:

        row = n//k #row number

        if not(n==k*row):
            num = node[n-1]
            nodecopy[n] = num
            nodecopy[n-1] = '-'

            move = (num,'right')
        
            if num!='-': neighbours.append([nodecopy,move])
            nodecopy = node[:]

        if not (n==k*(row+1)-1):
            num = node[n+1]
            nodecopy[n] = num
            nodecopy[n+1] = '-'

            move = (num,'left')
            
            if num!='-': neighbours.append([nodecopy,move])
            nodecopy = node[:]

        if not row==0:
            num = node[n-k]
            nodecopy[n] = num
            nodecopy[n-k] = '-'

            move = (num,'down')
            
            if num!='-': neighbours.append([nodecopy,move])
            nodecopy = node[:]


        if not row==k-1:
            num = node[n+k]
            nodecopy[n] = num
            nodecopy[n+k] = '-'

            move = (num,'up')
            
            if num!='-': neighbours.append([nodecopy,move])
            nodecopy = node[:]


    return neighbours

def backtrack(closed_queue,goal):
    #goal node is the last in the queue

    #start from last element and work backwards
    #Check if the config is the same as the parent of previous node
    
    n = len(closed_queue)
    moves = []
    parent = goal

    for i in range(n-1,0,-1):
        if closed_queue[i][0]==parent:        #node config is parent of prev
            moves.append(closed_queue[i][4])
            parent = closed_queue[i][3]

    moves.reverse()
    return moves

    
def npuzzle(k,start,goal,heuristic):

    if heuristic == "misplaced":
        def h(config,goal):
            return misplaced(config,goal)
        
    elif heuristic == "manhattan":
        def h(config,goal):
            return manhattan(config,goal)
    else:
        print("Error")

    #set up nested array/s to hold node info
    #fromat of a node info - config, g,h,parent config, move to get there
    
    open_queue = [[start,0,h(start,goal),[],(-1,'')]]
    closed_queue = []

    num_nodes = 0

    #while (len(open_queue))!=0:
    while True:
        num_nodes +=1

        #remove from open queue, the node with lowest f = g+h
        n = min_f(open_queue)
        node = open_queue[n]
        open_queue = open_queue[:n] + open_queue[n+1:]

        
        #mark node as closed
        closed_queue.append(node)

        #if the goal configuration is reached with minm f score, stop
        if node[0]==goal:
            break
        
        #check the node's neighbours
        neighbours = gen(node[0],k)

        for i in range(len(neighbours)):

            #if neighbour is in closed queue, ignore it
            if is_in_queue(closed_queue,neighbours[i][0]):
                continue

            #if neighbour is not in open queue, add it
            index = is_in_queue(open_queue,neighbours[i][0])
            
            if not index:
                open_queue.append([
                    neighbours[i][0],      #configuration
                    node[1]+1,             # g score
                    h(neighbours[i][0],goal),   #calculate h from config
                    node[0],               #parent config
                    neighbours[i][1]       #move taken
                    ])

            else:
                #if the neighbour config was already in OQ, check if it can be improved 

                if open_queue[index][1] > node[1]+1:
                    #substitute the 'neighbour' node's  g,parent and moves
                    open_queue[index][1] = node[1]+1
                    open_queue[index][3] = node[0]          #update parent config
                    open_queue[index][4] = neighbours[i][1] #move taken
          
        


    #While loop will break eventually
    # now, print the backtracked list
    
    
    moves = backtrack(closed_queue,goal)

    return [num_nodes,moves]

def readfile(path):

    file = open(path,'r')
    text = file.read()
    file.close()

    return re.split('\t|\n',text)[:-1]


def writefile(path,moves):

    strlist = []

    for tupl in moves:
        strlist.append('(%d,%s)'%(int(tupl[0]),tupl[1]))

    text = ', '.join(strlist)
    text += '\n'

    file = open(path,'w')
    file.write(text)
    file.close()

if __name__ == "__main__":

    start = readfile(sys.argv[1])

    goal = readfile(sys.argv[2])

    k = int(math.sqrt(len(start)))

    if len(sys.argv)==3:
    
        sequence_info = npuzzle(k,start,goal,"misplaced")

    elif len(sys.argv)==4 and (sys.argv[3]=="manhattan" or sys.argv[3]=="misplaced"):

        sequence_info = npuzzle(k,start,goal,sys.argv[3])

    else:

        print("Argument error")
        exit()

    print(sequence_info[0]) #number of nodes explored
    print(sequence_info[1]) #move list
    writefile('output.txt',sequence_info[1])

    

    

