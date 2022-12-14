# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:44:37 2022

@author: sgabalog
"""

#This is the agent frame work for the drunks.py file
#The main objective of the framework is to move the drunks.

#Import relavent libaries
import random

#Create class for drunks

class Drunk():
    #Creates variaables
    def __init__(self, environment, drunks, ids):
        
        #Create environment and drunks
        self.environment = environment
        self.drunks = drunks
        
        #Create house numbers
        self.house_ids = ids
        
        #Set starting point to pub
        self.x = 149
        self.y = 149
        
        #Set drunks being at home to false
        self.home = False
        
        #Create memory list for x and y coordinates
        self.mem_y = []
        self.mem_x = []
        
        #Create dummy varibles for movement and set to x and y coor dinates
        self.new_y = self.y
        self.new_x = self.x
        
        #add starting coordinates to the memory lists
        self.mem_y.append(self.y)
        self.mem_x.append(self.x)
        
        #list for random choice
        self.num_list = [20, -20]
        
    #Function to move drunks   
    def move(self):
        #First move drunks out of the pub
        if self.y >=139 and self.y <= 159 and self.x >= 139 and self.x <= 159:
            self.y = self.y + random.choice(self.num_list)
            self.x = self.x + random.choice(self.num_list)
            
            
        # if self.x >=139 and self.x <= 159:
        #     self.x = self.x + random.choice(self.num_list)
        
        #Using random library generate random number to move y coordinate
        if random.random() <= 0.5:
            #if statement for if drunk is close to the edge of the map they
            #move away from bottom edge
            if self.y <= 10:
                self.y = self.y + 10
            else:
                #make new y equal y coordinate
                self.new_y = self.y
                #change new y coordinate by a random value between 1,10
                self.new_y = self.new_y - (random.randint(1,10))
                
                #loop through y coordinate memory list
                for i in self.mem_y:
                    #if already in memory then no change in y coordinate
                    if i == self.new_y:
                        self.y = self.y
                    #if not in memory
                    else:
                        self.y = self.new_y
                        #coordinate is added to list
                        self.mem_y.append(self.new_y)
                        #oldest rememebered coordinate is cut off
                        self.mem_y = self.mem_y[-150:]
                        break
                    
        else:
            #if statement for if drunk is close to the edge of the map they
            #move away from top edge
            if self.y >= 290:
                self.y = self.y - 10
            else:
                #make new y coordinate equal y coordinate
                self.new_y = self.y
                #change value of new y coordinate by random value between 1,10
                self.new_y = self.new_y + (random.randint(1,10))
                
                #loop through y coordinate memory list
                for i in self.mem_y:
                    #if new y coordinate in memory then do not change y
                    #coordinate to new
                    if i == self.new_y:
                        self.y = self.y
                        self.mem_y = self.mem_y[-150:]
                    #if not in memory 
                    else:
                        #y coordinate equals new y coordinate
                        self.y = self.new_y
                        #add new coordinate to memory
                        self.mem_y.append(self.new_y)
                        #remove oldest coordinate from memory
                        self.mem_y = self.mem_y[-150:]
                        break
                    

        #generate random number to move x coordinate      
        if random.random() <= 0.5:
            #moves drunk away from left edge
            if self.x <= 10:
                self.x = self.x + 10
            else:
                #equals new x to x coordinate
                self.new_x = self.x
                #shifts new x coordinate
                self.new_x = self.new_x - (random.randint(1,10))
                
                #loops throug x cooridnate memory list
                for i in self.mem_x:
                    #if new coordinate in memory do not move
                    if i == self.new_x:
                        self.x = self.x
                    #if new coordinate is not in memory
                    else:
                        #x coordinate equals new x coordiante
                        self.x = self.new_x
                        #add new coordinate to memory list
                        self.mem_x.append(self.new_x)
                        #remove oldest x coordinate from memory
                        self.mem_x = self.mem_x[-150:]
                        break
                    
        else:
            #moves drunks away from right edge
            if self.x >= 290:
                self.x = self.x - 10
            else:
                #equals x coordinate to new x
                self.new_x = self.x
                #shift new x coordinate
                self.new_x = self.new_x + (random.randint(1,10))
                #loop through memory list
                
                for i in self.mem_x:
                    #if new coordinate in memory do not move
                    if i == self.new_x:
                        self.x = self.x
                        self.mem_x = self.mem_x[-150:]
                    #if not in list move
                    else:
                        #x coordinate equals new coordinate
                        self.x = self.new_x
                        #add new coordinate to list
                        self.mem_x.append(self.new_x)
                        #remove oldest x coordinate from memory
                        self.mem_x = self.mem_x[-150:]
                        break

