import csv


def getLocationsAndTravelTimesFromCsv():
    with open("..\\inputFiles\\" + "travelTimes.csv") as csvfile:
        data = list(csv.reader(csvfile))

    locationList = data[0][1:]

    travelTimes = {}
    for i,fromLoc in enumerate(locationList):
        for j, toLoc in enumerate(locationList):
            if data[j+1][i+1].isdigit() and i+1 != j+1:
                travelTimes[(fromLoc, toLoc)] = int(data[j+1][i+1])

    return locationList, travelTimes



def printToConsole(decisionVar, locationList):

    fromLoc = locationList[0]
    visited = []

    while True:

        for toLoc in locationList:

            if fromLoc != toLoc and toLoc not in visited:
                if decisionVar[fromLoc][toLoc].value() > 0.5:
                    print("Travel from " + str(fromLoc) + " to " + str(toLoc))
                    break


        if len(visited) == len(locationList) - 1:
            assert decisionVar[fromLoc][locationList[0]].value() > 0.5, "Error in logic/optimization"
            print("Travel from " + str(fromLoc) + " to " + str(locationList[0]))
            break

        visited.append(fromLoc)
        fromLoc = toLoc

    print()