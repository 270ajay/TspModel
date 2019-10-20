# Optimization of Traveling Salesman Problem in PuLP using Lazy sub-tour elimination constraints

**Description**

-	Optimizing the Traveling Salesman Problem using Mixed Integer Programming. 
-   Sub-tour elimination constraints are added 'LAZILY' i.e., on-demand. 
-   Every location must be visited only once 
-   All locations must be visited 
-   Minimize travel time
-   Symmetrical travel times (undirected graph)
-	Location names and their travel times are from travelMatrix.csv in inputFiles folder


## Prerequisites

To run this **Python** program, please install the following libraries/packages:

-   **pulp**
-   **csv**
-   **itertools**



## About the project

-    All the code is in src folder. 
-    travel time files is in inputFiles folder
-    Lp file generated will be in output folder
-    To run the code, please run optimizationProgram.py (to run from cmd, please enter `python.exe optimizationProgram.py`)


## Sample LP File 

```shell
\* Var: Travel_FromPointId_ToPointId - Traveling Salesman Problem *\
Minimize
OBJ: 0.7 Travel_1_2 + 0.8 Travel_1_3 + 1.3 Travel_1_4 + 0.5 Travel_1_5
 + 0.8 Travel_1_6 + 1.2 Travel_2_3 + 1.6 Travel_2_4 + 0.6 Travel_2_5
 + 1.2 Travel_2_6 + 0.9 Travel_3_4 + 0.7 Travel_3_5 + 1.5 Travel_3_6
 + 0.9 Travel_4_5 + 1.9 Travel_4_6 + 1.7 Travel_5_6
Subject To
LazySubTourElimConstraint1: Travel_1_2 + Travel_1_6 + Travel_2_6 <= 2
Twoedgeseachloc1: Travel_1_2 + Travel_1_3 + Travel_1_4 + Travel_1_5
 + Travel_1_6 = 2
Twoedgeseachloc2: Travel_1_2 + Travel_2_3 + Travel_2_4 + Travel_2_5
 + Travel_2_6 = 2
Twoedgeseachloc3: Travel_1_3 + Travel_2_3 + Travel_3_4 + Travel_3_5
 + Travel_3_6 = 2
Twoedgeseachloc4: Travel_1_4 + Travel_2_4 + Travel_3_4 + Travel_4_5
 + Travel_4_6 = 2
Twoedgeseachloc5: Travel_1_5 + Travel_2_5 + Travel_3_5 + Travel_4_5
 + Travel_5_6 = 2
Twoedgeseachloc6: Travel_1_6 + Travel_2_6 + Travel_3_6 + Travel_4_6
 + Travel_5_6 = 2
Binaries
Travel_1_2
Travel_1_3
Travel_1_4
Travel_1_5
Travel_1_6
Travel_2_3
Travel_2_4
Travel_2_5
Travel_2_6
Travel_3_4
Travel_3_5
Travel_3_6
Travel_4_5
Travel_4_6
Travel_5_6
End
```