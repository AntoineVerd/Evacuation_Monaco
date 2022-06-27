# Semester project: Validating Evacuation Simulations for Civilian Evacuation Planning 


This repository is supposed to be consulted by Mr Wilfredo J. Robinson M. and Mr Motonobu Kanagawa to check and review.
This repository includes the semester project code for the simulation of an evacuation in Monaco.
It includes the files to simulate an evacuation of 10% of the population of Monaco as well as a wave arriving on the coast of Monaco at 30s in the simulation.
The repositories needed for the simulation are :
- population_distribution including the shapefile, the prj file and the database file associated to the population
- road_network including the shapefile, the prj file and the database file associated to the roads
- shelter_locations including the the shapefile, the prj file and the database file associated to the shelters 
- tsunami_inundation including the asc files, the prj files and the coordinates of the tsunami
Finally, there is the file Evacuation Model (.netlogo) containing the main code for the simulation.

The files that we modified are the .shp, .shx, .prj and .dbf in the first three cited repositories and the .asc, .prj, .csv and .txt files in the tsunami repository. 
The most important files to check are the shapefiles, the database files and one or two asc files of the tsunami repository.

The .asc files were generated thanks to the python scripts available in the "Python codes" repository. The code "Adaptation_gauges.py" was used to restructurate the gauges files, the code "asc_file_creation.py" was used to create the asc file based on the modified gauges and the code "sample.py" was used to create the sample.asc file.

To run the simulation, the repositories and the NetLogo code need to be placed in the same folder to then launch the simulation in NetLogo thanks to the evacuation model file.