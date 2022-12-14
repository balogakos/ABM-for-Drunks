# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:20:11 2022

@author: sgabalog
"""
#Import relavent libaries

import csv
import agentframeworkdrunks
import matplotlib
import matplotlib.animation
import matplotlib.pyplot

#Set random seed for testing
#random.seed(2)

#Create update function to be called for animation
def update(frame_number):
    #test to see when agents get home
    #agent_home = 0
    global carry_on
    #Clear figure
    fig.clear()
    
    #If input user chooses to see running model this code runs
    if choice == 1:
        for i in range(num_drunks):
            if drunks[i].home==False:
                drunks[i].move()
                #add 1 to density map where the agent is
                densitymap[drunks[i].y][drunks[i].x]+=1
                #if the house no. of drunk matches environment then it stops
                if drunks[i].house_ids==drunks[i].environment[drunks[i].y][drunks[i].x]:
                    drunks[i].home=True
                    #print number when an agent is home
                    #agent_home = agent_home + 1
                    #print(agent_home)
                    
    #If input user chooses to see final model this code runs
    elif choice == 2:
        #loop through list of drunks and move each agent
        for i in range(num_drunks):
            while drunks[i].home==False:
                drunks[i].move()
                #add 1 to density map where the agent is
                densitymap[drunks[i].y][drunks[i].x]+=1
                #if the house no. of drunk matches environment then it stops
                if drunks[i].house_ids==drunks[i].environment[drunks[i].y][drunks[i].x]:
                    drunks[i].home=True
                    #print number when an agent is home
                    #agent_home = agent_home + 1
                    #print(agent_home)
    
    #Both subplots update with the animation
    #Create subplot for town map and show environmnet and drunks
    ax = fig.add_subplot(121)
    ax.imshow(environment, cmap="binary")
    for i in range(num_drunks):
        ax.scatter(drunks[i].x,drunks[i].y, s=8, c="red", marker="8")
    ax.title.set_text("Town Map")
    ax.set_ylim(0,300)
    ax.set_xlim(0,300)
    
    #Create subplot for density map
    ax = fig.add_subplot(122)
    ax.imshow(densitymap, cmap="binary")
    for i in range(num_drunks):
        ax.scatter(drunks[i].x,drunks[i].y, s =0, c="red")
    ax.title.set_text("Density Map")
    ax.set_ylim(0,300)
    ax.set_xlim(0,300)
    
    #write output file with density map list
    f2= open ('densitymap.csv', 'w', newline= '')
    writer = csv.writer (f2, delimiter = ' ')
    for row in densitymap:
        writer.writerow(row)
    f2.close()
        
#Function for the number for iterations
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10000) & (carry_on):
        yield a
        a = a + 1
        

#Set choice as 0 for choice
choice = 0

#Input choice bewteen running model or final model
#Using simple input statement which creates 2 options
#Choice determines which form of the model is run


tt = int(input("1 to see running model [Disclaimer: This takes a while] \n"
               "2 to see final model [With drunks home] \n"
               "Enter choice --> "))

if tt == 1:
    choice = 1
else:
    choice = 2

#Set parametres
num_drunks = 25

#Create lists
drunks = []

# list for environment
environment = []

#List for output file
densitymap = []

#Using a for loop add agents to the environment
#Give each drunks a house number between 10-250
#Connect with agentframework

for i in range(num_drunks):
    ids = (i + 1)*10
    drunks.append(agentframeworkdrunks.Drunk(environment, drunks, ids))
    #Tested by printing ids and coordinates
    #print([drunks[i].y][drunks[i].x])
    #print(drunks.[i].ids)
    
#Create variable carry_on and set it to True                
carry_on = True

#Open map file and read through it and add to environment list
with open('drunks.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    #using two for loops read through it by row then by number
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
#Tested by printing environment and visualing comparing to input file
#print(environment)
        
#Create plot wih set dimensions
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Tested by showing plot
#matplotlib.pyplot.imshow(environment)

#make densitymap dimensions equal environment
height = len(environment)
width = len(environment[0])

#Using for loops and a rowlist add all 0's to the density map list
for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0)
    densitymap.append(rowlist)
#Tested by printing density map list to see if all values = 0
#print(densitymap)

#Animation with gen and update functions
animation = matplotlib.animation.FuncAnimation(fig, update, 
                                               frames=gen_function, 
                                               repeat=False)