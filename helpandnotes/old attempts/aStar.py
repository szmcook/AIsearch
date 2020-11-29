def f( i ):
    '''returns the f value of a node'''
    return g(i) + h(i)

def g( i ):
    # step cost should be stored with each node
    stepCostToNode = 0
    return stepCostToNode

def h(partialTour):
    '''returns the heuristic cost of a partial tour'''
    if len(partialTour) == num_cities:
        return 0
    else:
        # calculate the heuristic cost
        # an example heuristic cost is the sum of the minimum distances of all possible routes from each city which is not presented in the current visit node label and the present city
        # if the present node is [1,4] then h(4) = min( (all routes from 2 to 1), (all routes from 3 to 1), (all routes from 4 to 1) )
        return 10

def aStarSearch(dist_matrix):
    '''searches the tree for a goal node'''

    # let VISIT be a list to save visited nodes
    # PATH is a set to save distances from the root node to the goal

    VISIT = []
    VISIT.append(1)
    
    while len(VISIT) != 0:
        n = VISIT[0]
        if n is a goal node:
            output result
        VISIT.push(children of N)
        VISIT.sortbyf()