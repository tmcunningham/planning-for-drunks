# Programming for Social Science Assessment 2: Planning for Drunks

This repository contains code to run an agent based model that simulates drunks leaving a pub and trying to get home. Initially, the drunks cannot remember where their house is and move randomly, but they gradually sober up and begin to move towards their home. This code was produced for the second assessment of the GEOG5995 module taught by the University of Leeds.

## Contents

Within the **python** folder, this repository contains the following:
- **drunk_functions.py**: file that contains the functions needed to run the model
- **drunksframework.py**: file containing the drunk class
- **drunk_model.py**: file that uses the functions from drunk_functions.py to create an animation of the model and write the output to a txt file
- **measure_drunks_moves.py**: file that measures how many iterations it takes for all drunks to get home with different ```drunk_level```s and plots the results as a boxplot
- **drunk.plan**: raster data file with the drunks' homes and the pub
- **test_drunk_functions.py**: module with unit tests for functions in drunk_functions.py and mmethods in drunksframework.py

## About the animation (drunk_model.py)

### What the model does

When it is run, the file **drunk_model.py** runs the following stages and produces an animation:
- imports a raster file of the town's buildings (drunks' houses and the pub)
- using the town data, creates a named dictionary of buildings' ```x``` and ```y``` co-ordinates
- sets the pub's front and back door to be the south-west and north-east corners, respectively (where the drunks will start from)
- creates a list of instances of the ```drunk``` class, as defined in **drunksframework.py**
- for each iteration:
  - adds 1 to the ```town``` raster data at each drunk's location and then moves each drunk (randomly if they are still drunk, or towards their house if their ```drunk_level``` is 0)
  - sobers each drunk up (reduces the ```drunk_level``` by 1) if they have visited their current co-ordinates before

In the animation, the dots represent the drunks and the squares are the buildings. The drunks will change colour as they get less drunk - red is completely sober and blue is the most drunk they can be.

### How to run the model

The user can run the model and produce the animation from the command line by using the following line of code in the directory where **drunk_model.py**, **drunk_functions.py**, **drunksframework.py** and **drunk.plan** are saved:

```python drunk_model.py [num_of_moves] [drunk_level_lower] [drunk_level_higher]```

where the arguments in brackets can be replaced by user inputs. These arguments are (default values given after equals sign):
- ```[num_of_moves] = 5000```: maximum number of iterations
- ```[drunk_level_lower] = 20```: minimum value for each drunk's starting ```drunk_level```
- ```[drunk_level_higher] = [drunk_level_lower] + 200```: maximum value for each drunk's starting ```drunk_level```

Each drunk's starting ```drunk_level``` will be chosen at random between the lower and higher levels inclusive (so if the numbers are the same, all drunks will start at the same ```drunk_level```). If these arguments aren't provided (or only some are), the user will be prompted to input them 3 times before the programme uses the default values.

### Stopping conditions

The model will run until either of the following conditions is met:
- all drunks reach their home (each drunk has a specific house), or
- the maximum number of iterations is reached.

### Outputs

As well as the animation, **drunk_model.py** will produce a text file output:
- **town_out.txt**: an updated version of the **drunk.plan** raster file, with 1 added to each (x,y) co-ordinate for each time a drunk has visited it.

## Measuring drunk levels (measure_drunks_moves.py)

Another script, **measure_drunks_moves.py**, was created to measure how long it takes all drunks to get home when they start at different ```drunk_level```s. For each ```drunk_level``` in the list ```[10, 20, 50, 100, 200]```, the script will run 1000 iterations of the model (without outputs) with all drunks set at the current ```drunk_level```. The script will then produce and save a boxplot of the number of moves it took all the drunks to get home.

**Please note**: This script can take around 25 minutes to run.

## License

The code in this repository is licensed under the MIT License. Please see [LICENSE](https://github.com/tmcunningham/planning-for-drunks/blob/master/LICENSE) for details.

