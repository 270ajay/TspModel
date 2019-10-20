import pulp
import itertools


def createAndRunTSPModel(travelTimes, locationList):

    tsp = pulp.LpProblem("Traveling Salesman Problem - DecisionVar : travel_fromLocation_toLocation ", pulp.LpMinimize)

    decisionVar = pulp.LpVariable.dicts("Travel",(locationList,locationList),0,1,pulp.LpInteger)

    for fromLoc,toLoc in travelTimes.keys():
        decisionVar[toLoc][fromLoc] = decisionVar[fromLoc][toLoc]

    # Objective
    tsp += sum([float(travelTimes[fromLoc,toLoc]) * decisionVar[fromLoc][toLoc] for fromLoc,toLoc in travelTimes.keys()])

    # Constraint
    for fromLoc in locationList:
        tsp += pulp.lpSum([decisionVar[fromLoc][toLoc] for toLoc in locationList if fromLoc!=toLoc]) == 2, \
               "twoEdgesFor"+str(fromLoc)

    numOfSubTourCtsAdded, tsp, decisionVar = solveAndAddSubtourElimConstraints(tsp, decisionVar, locationList)

    return tsp, decisionVar, numOfSubTourCtsAdded



def returnOptimalEdges(decisionVar, locationList):

    optimalEdges = []
    for i, fromLoc in enumerate(locationList):
        for j, toLoc in enumerate(locationList):
            if i < j:
                if decisionVar[fromLoc][toLoc].value() > 0.5:
                    optimalEdges.append((fromLoc, toLoc))  # appending edges from optimal solution into it.

    return optimalEdges



def returnSubtour(optimalEdges, locationList):

    unvisited = []
    for loc in locationList:
        unvisited.append(loc)

    cycle = range(len(locationList) + 1)  # initial length has 1 more location

    while unvisited:  # true if list is non-empty
        thisCycle = []
        neighbors = unvisited

        while neighbors:
            current = neighbors[0]
            thisCycle.append(current)
            unvisited.remove(current)
            neighbors = []

            for fromLoc, toLoc in optimalEdges:
                if fromLoc == current and toLoc in unvisited:
                    neighbors.append(toLoc)
                elif toLoc == current and fromLoc in unvisited:
                    neighbors.append(fromLoc)

        if len(cycle) > len(thisCycle): # to return smaller sub-tour
            cycle = thisCycle

    return cycle




def solveAndAddSubtourElimConstraints(tsp, decisionVar, locationList):

    iter = 0
    while True:

        tsp.solve()
        optimalEdges = returnOptimalEdges(decisionVar, locationList)
        cycle = returnSubtour(optimalEdges, locationList)

        if len(cycle) >= len(locationList):  # If not, then there is a subtour and we add constraint.
            break

        # Add Sub-tour elimination constraint
        combinations = itertools.combinations(cycle, 2)
        tsp += pulp.lpSum([decisionVar[fromLoc][toLoc] for fromLoc, toLoc in combinations]) <= len(cycle) - 1, \
               "LazySubTourElimConstraint" + str(iter + 1)

        iter += 1
        print("Adding sub-tour elimination constraint and solving again...")

    return iter, tsp, decisionVar