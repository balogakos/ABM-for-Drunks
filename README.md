# ABM-for-Drunks
Agent based model for drunks leaving a pub attempting to find their way home.

This program reads in a txt file of a pub and 25 homes. It maps this onto a figure and creates drunks which move randomly around the figure until they find their way home. Once they find their way homne the drunks stop moving. The program also produces a figure of the density of the drunks passing through each point on the map. The program finishes when all of the drunks are at home.

Submission Contents:

1. drunks.py -> The main code
2. agentframeworkdrunks.py -> agent framework for drunks.py
3. drunks.txt -> input text file for pub and home locations
4. DocumentationPFSS.docx -> documentation explaining development, sources, issues, and limitations
5. test_move_function.py -> presentation of testing of move function
6. densitymap.csv -> this is the csv file the program will produce

Instructions to run the code:

1. The code was produced in python 3.9 using Spyder as part of Ananconda.
2. Copy the agentframeworkdrunks.py, in.txt and drunks.py into Spyder or editing softerware of choice. Saving the drunks.txt in the same directionary.
3. Before running the code "%matplot qt" is required to be entered for animations to run.
4. Run the drunks.py file.
5. The program will prompt for the choice between 1: Running Model or 2: Finished Model.
6. Enter choice.
7. Program will run desired choice
8. A csv file of the density file will be produced
