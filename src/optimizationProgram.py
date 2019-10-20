import tspModel
import utilities
import pulp



if __name__ == '__main__':

    try:

        locationList, travelTimes = utilities.getLocationsAndTravelTimesFromCsv()

        tsp, decisionVar, numOfSubTourCtsAdded = tspModel.createAndRunTSPModel(travelTimes, locationList)

        print("\nNumber of Lazy Sub-Tour Elimination Constraints added: ", numOfSubTourCtsAdded, "\n")

        print(pulp.LpStatus[tsp.status])

        utilities.printToConsole(decisionVar, locationList)

        print("Objective value:", pulp.value(tsp.objective))

        tsp.writeLP("..\\output\\" + "TspLPModel.lp")


    except Exception as e:

        print("Program failed due to : ", e)