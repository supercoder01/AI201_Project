maximum=1000 # Initial value of beta. 1000 is considered to be positive infinity here
minimum=-1000 # Initial value of alpha.-1000 is considered to be negative infinity here

# Function to perform alpha beta pruning
def alpha_beta(Current_dep,Node_number,max_player,score,alpha,beta):
    if Current_dep==3: # specified depth from start
        return score[Node_number]

    if max_player: # if max_player==true the block of code below will run
        best=minimum
        for i in range(0,2): # to search in each child of a node
            value=alpha_beta(Current_dep+1,Node_number*2+i,False,score,alpha,beta)
            best=max(best,value)
            alpha=max(alpha,best)
            # If alpha is greater or equal to beta then pruning will take place
            if beta<=alpha:
                break
        return best

    else:
        best=maximum
        for i in range(0,2):
            value=alpha_beta(Current_dep+1,Node_number*2+i,True,score,alpha,beta)
            best=min(best,value)
            beta=min(beta,best)
            if beta<=alpha:
                break
        return best
# list to store initial terminal node values
score=[]
l_node=int(input("Enter the number of leaf nodes : "))         #  totoal number of leaf nodes
for i in range(l_node):
    value=int(input(f"Enter the value of leaf node {i} : "))  # assigning the value to terminal nodes
    score.append(value)

Current_dep=int(input("Enter the current depth : "))          # getting input of current node from user
Node_number=int(input("Enter the node number : "))            # current node number

Max_Turn=True       #  Decides the current player's turn

answer=alpha_beta(Current_dep,Node_number,True,score,minimum,maximum)   # Maximum value will be returned to parent node after evaluating all its child nodes
print("The optimal value is : ",answer)