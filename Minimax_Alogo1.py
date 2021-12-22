import math
import random

def minmax(Current_dep,Node_number,Max_Turn,score,T_depth):
    if Current_dep==T_depth: # The search will contine till we have reached target depth which we specified.
        return score[Node_number]

    if Max_Turn==True: # If its maximizing player turn then the following statements will run
        return max(minmax(Current_dep+1,Node_number*2,False,score,T_depth), # Largest value of children will be returned to parent node after comparing n childrens.
                   minmax(Current_dep+1,Node_number*2+1,False,score,T_depth))

    else: # Following statements will run if its minimizing player's turn
        return min(minmax(Current_dep+1,Node_number*2,True,score,T_depth), # minimum value will be returned to parent node after comparing the values of n children.
                   minmax(Current_dep+1,Node_number*2+1,True,score,T_depth))

# to store terminal nodes values
score=[]

l_node=int(input("Enter the number of leaf nodes : "))         #  totoal number of leaf nodes
for i in range(l_node):
    value=int(input(f"Enter the value of leaf node {i} : "))  # assigning the value to terminal nodes
    score.append(value)

T_depth=math.log(l_node,2)                                    #  for calculating the depth of node

Current_dep=int(input("Enter the current depth : "))          # getting input of current node from user
Node_number=int(input("Enter the node number : "))            # current node number

Max_Turn=True       #  Decides the current player's turn

print("Answer = ",end=" ")
answer=minmax(Current_dep,Node_number,Max_Turn,score,T_depth)   # Maximum value will be returned to parent node after evaluating all its child nodes
print(answer)