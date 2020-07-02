# Solution for msg Code Challenge
## Task
Given a set of locations, you are supposed to find a path between these locations so that you visit 
each one of them exactly once. You shall finish at the location you start from (Ismaning/München (Hauptsitz)) and you 
shall minimize the travel distance. ([Link to challenge](https://www.get-in-it.de/coding-challenge#mitmachen))

## Approach
This is a classic travelling salesman problem. As such the problem is NP-hard and there are no algorithms (yet) that 
can find a optimal solution with certainty, but some that use useful heuristics. I decided to not develop an 
algorithm by myself but instead use some already proven ones and give the user the choice to select one depending on
the requirements of the problem.

Furthermore I also implemented the option to use different approaches to calculate the distance between locations in 
order to be able to consider different requirements.

## Installation
To run this solution the following steps are needed:
1. Clone the Repo
    ```shell
    git clone https://github.com/gerpo/msg-code-challenge.git
    ```
2. Change into directory
    ```shell
   cd msg-code-challenge
   ```
3. Create virtual environment (optional but highly recommended to not fill global space)
    ```shell
   python -m venv venv
   ```
4. Activate virtual environment (not needed if step 3 skipped)
    - On Linux
        ```shell
       . venv\bin\activate
       ```
       or
       ```shell
       source venv\bin\activate
       ```
    - On Windows
        ```shell
       \venv\Scripts\activate
       ```
5. Install required packages
    ```shell
   pip install -r requirements.txt
   ```

## Getting Started
After the [installation](#Installation) you are ready to run the program. 
To execute it with the given location data and and the default options you just need to run 
```shell
python main.py
```

## Options
In the main.py are some options that can be changed by the user.

For all options that are supported right know you can use defined constants to set the options accordingly.
## Input File
- Option name: input_file
- Default option: ```'msg_standorte_deutschland.csv'```
- Type: String
- Options: Path to csv file.
> The provided csv file should have the same format than the provided example file. 

### Distance Calculator
- Option name: distance_type
- Default option: ```Constants.VINCENTY_DISTANCE```
- Type: String
- Options:
    - ```Constants.EUCLIDEAN_DISTANCE```  
        Uses the simple euclidean distance between two locations. The calculation is very easy and because of that fast, 
        but since it does not consider the curvature of the earth it is the least accurate. Only useful if the locations
        are close to each other and the effect of the curvature is minimal or to get a first rough solution for a hugh 
        amount of locations.
    - ```Constants.HAVERSINE_DISTANCE```  
        Uses the haversine formula which considers the curvature of the earth to determine the distance between two locations.
        It is more accurate than ```Constants.EUCLIDEAN_DISTANCE``` but the calculation is slightly more complex 
        (should only be relevant for a big amount of locations).
    - ```Constants.VINCENTY_DISTANCE```  
        Vincenty formula is used to calculate the distance between two coordinates. 
        Considers the oblate spheroid shape of the earth and therefore should be the most accurate, but calculation is slower.
    - ```Constants.GREAT_CIRCLE_DISTANCE```  
        Same as ```Constants.HAVERSINE_DISTANCE```, but uses the ```distance.great_circle``` of the ```geopy``` package.
        
> You can add your own distance calculation algorithm. You just need to create a class that extends the 
>[```DistanceCalculatorInterface```](DistanceCalculator/DistanceCalculatorInterface.py) and add it as an option to the 
>[```DistanceCalculatorBuilder```](DistanceCalculator/DistanceCalculatorBuilder.py).

## Solver
- Option name: solver_type
- Default option: ```Constants.ORTOOLS_SOLVER```
- Type: String
- Options:
    - ```Constants.MLROSE_SOLVER```  
        Uses an genetic algorithm with a random start state. It is by far the slowest algorithm of the implemented ones, 
        but seems to deliver the best solution. Use it if you want a relatively good solution and time is not restricted.
        Depending on the problem on hand the solution can in some cases be improved by changing the algorithm options
        (max_iter, random_state, etc.).
    - ```Constants.LKH_SOLVER```  
        This solver is an implementation of the Lin-Kernighan heuristic for solving the traveling salesman problem. 
        It is pretty fast but delivers, at least for the given problem, a slightly less optimal solution compared to the 
        ```Constants.MLROSE_SOLVER``` option.
    - ```Constants.ORTOOLS_SOLVER```  
        With this option a solver of google's orTools is used. It is fast and delivers good results, but can only handle 
        integer distances. So that distances are rounded and as such it is by definition less accurate than the other 
        two options.
> You can add your own solver implementation. You just need to create a class that extends the 
>[```SolverInterface```](Solver/SolverInterface.py) and add it as an option to the 
>[```SolverBuilder```](Solver/SolverBuilder.py). 

> There are faster and more reliable implementations of algorithms that can solve this kind of problem, but a lot of
>them need additional binaries or software on the host computer. This makes the installation way more complex. To keep it
>simple I only used algorithms that can be installed using only pip. For a more permanent solution or to further optimize
>better (and external) implemented solutions should be preferred.

## Displaying the Solution
>Order of visit for the locations (0 index, first location in input file has the index 0) and full distance is always 
>shown in the terminal after running the program.

- Option name: print_itinerary
- Default option: ```True```
- Type: Boolean
- Descriptions: Determines if the whole itinerary is printed to the console after solving.

<!-- -->

- Option name: show_visualization
- Default option: ```True```
- Type: Boolean
- Descriptions: Determines if the solution is visualized after solving.
- Info: Uses ```plotly``` and opens a browser window to show the interactive visualization.

<!-- -->

- Option name: visualization_options
- Default option: ```{'animate_visualization': True, 'export_as_image': False}```
- Type: dict
- Descriptions: Contains a dictionary with two options.
    - ```animate_visualization```  
        If ```True``` path will be animated after clicking a play button.  
        If ```False``` full circle path is shown directly.
    - ```export_as_image```  
        If ```True``` image if full circle path is saved.  
        If ```False``` only the interactive visualization is shown.
- Info: this options is only relevant if ```show_visualization``` is ```True```.

# Results
| Solver \ Distance Calc. 	| euclidean                                                                               	| haversine                                                                               	| vincenty                                                                               	| great_circle                                                                                	|
|-------------------------	|-----------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------	|---------------------------------------------------------------------------------------------	|
| mlrose                  	| 2328.28 km<br> 250.50 s<br> [Result](results/images/mlrose_euclidean.svg)   	| 2333.41 km<br> 212.27 s<br> [Result](results/images/mlrose_haversine.svg)   	| 3024.31 km<br> 193.22 s<br> [Result](results/images/mlrose_vincenty.svg)   	| 2333.42 km<br> 171.64 s<br> [Result](results/images/mlrose_great_circle.svg)     	|
| LKH                     	| 2385.44 km<br> 0.04 s<br> [Result](results/images/lkh_euclidean.svg)     	| 2366.26 km<br> 0.02 s<br> [Result](results/images/lkh_haversine.svg)    	| 2370.26 km<br> 0.03 s<br> [Result](results/images/lkh_vincenty.svg)    	| 2366.27 km<br> 0.02 s<br> [Result](results/images/lkh_great_circle.svg)     	|
| orTools                 	| 2318.00 km<br> 0.32 s<br> [Result](results/images/ortools_euclidean.svg) 	| 2322.00 km<br> 0.05 s<br> [Result](results/images/ortools_haversine.svg) 	| 2327.00 km<br> 0.04 s<br> [Result](results/images/ortools_vincenty.svg) 	| 2322.00 km<br> 0.06 s<br> [Result](results/images/ortools_great_circle.svg) 	|

Regarding shortest distance the best result is reached with the combination of the mlrose solver and the euclidean distance.
But if you take a look at the generated plot we can clearly see an unintuitive path that should not be the shortest.
Reason for that is probably that the distance between the locations is big enough for the curvature of the earth to have a significant effect. 
Therefore for this problem we cannot ignore the curvature and cannot use the euclidean distance. 

The next best result are delivered with the combination of mlrose solver and haversine / great circle distance. 
in both cases the paths look plausible and are only slightly longer than the first case, which makes sense considering
the curvature of the earth is now considered as well.

For the combination mlrose solver and vincenty distance a significant bigger distance was calculated and the path looks 
messy. That can be indicative of an unfinished run. The algorithm probably hit the set iteration limit and did not reach 
a optimal solution. 

The LKH solver calculated a slightly longer distance and a minimal different path than the mlrose solver, but in significant 
less time. The algorithm delivered almost immediate results even though the path was not the optimal.

Similar fast performance was reached by the orTools solver and it calculated the same optimal path as the mlrose solver.
Unfortunately the calculated distances can not be used directly. The solver uses integer values and rounds the initial
distances between location, so that the calculated objective value inaccurate is.

In order to get the best of both, fast performance and best solution, one could use the calculated order by the orTools 
and recalculated the distances based on that. In the here presented case this will work, but it can happen that because
the solver itself uses the rounded values the resulting order would not reflect the optimal solution without the rounding.

>**Conclusion:** The mlrose solver in combination with the classical haversine / great circle distance delivers a good 
>path with a distance of roughly 2333 km to complete the msg location tour.
>But if performance and a quick overview is more important another, a faster, algorithm is recommended.
