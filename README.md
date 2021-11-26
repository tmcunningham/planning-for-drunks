# Programming for Social Science Assessment 2: Planning for Drunks

This repository contains code to run an agent based model that simulates drunks leaving a pub and trying to get home. This code was produced for the second assessment of the GEOG5995 module taught by the University of Leeds.

## Contents

Within the **python** folder, this repository contains the following:
- **drunk_functions.py:** file that contains the functions needed to run the model
- **drunksframework.py:** file containing the drunk class
- **drunk_model.py** file that uses the functions from durnk_functions.py to create an animation of the model and write the output to a txt file
- **measure_drunks_moves.py** file that measures how many iterations it takes for all drunks to get home with different ```drunk_level```s
- **drunk.plan:** raster data file with the drunks' homes and the pub