# Programming for Social Science Assessment 2: Planning for Drunks

This repository contains code to run an agent based model that simulates drunks leaving a pub and trying to get home. This code was produced for the second assessment of the GEOG5995 module taught by the University of Leeds.

## Contents

Within the **python** folder, this repository contains the following:
- **drunk_functions.py:** file that contains the functions needed to run the model
- **drunksframework.py:** file containing the drunk class
- **drunk_model.py** file that uses the functions from durnk_functions.py to create an animation of the model and write the output to a txt file
- **measure_drunks_moves.py** file that measures how many iterations it takes for all drunks to get home with different ```drunk_level```s and plots the results as a boxplot
- **drunk.plan:** raster data file with the drunks' homes and the pub

## About the model

### What the model does

When it is run, the file **drunk_model.py** runs the following stages and produce an animation:
- imports a raster file of the town's buildings (drunks' houses and the pub)
- using the town data, creates a named dictionary of buildings' ```x``` and ```y``` co-ordinates
- sets the pub's front and back door to be the south-west and north-east corners, respectively (where the drunks will start from)
- creates a list of instances of the ```drunk``` class, as defined in **drunksframework.py**
- for each iteration:
  - moves each drunk (randomly if they are still drunk, or towards their house if their ```drunk_level``` is 0)
  - sobers each drunk up (reduces the ```drunk_level``` by 1) if they have visited their current co-ordinates before
 
The model will run until each drunk has reached their house or the maximum number of iterations has been reached. Each drunk has a specific house.

### How to run the model

The user can run the model and produce the animation from the command line by using the following line of code in the directory where **drunk_model.py**, **drunk_functions.py**, **drunksframework.py** and **drunk.plan** are saved:

```python drunk_model.py [num_of_moves] [drunk_level_lower] [drunk_level_higher]```

The arguments are:
- ```[num_of_moves] = 5000```: maximum number of iterations
- ```[drunk_level_lower] = 20```: minimum value for each drunk's starting ```drunk_level```
- ```[drunk_level_higher] = 100```: maximum value for each drunk's starting ```drunk_level```

Each drunk's starting ```drunk_level``` will be chosen at random between the lower and higher levels inclusive (so if the numbers are the same, all drunks will start at the same ```drunk_level```).

