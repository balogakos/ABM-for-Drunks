# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:21:59 2022

@author: sgabalog
"""
#The purpose of this document is to show how the movement function for the
#agent framework. The idea is that the function checks the value of the
#coordinate, if its the pub or close to the edge, the drunk is turned
#away and shifts away. The rest of the code moves the drunk by a random number
# of steps (between 1 and 10). Then the function checks if the drunk was at the
# new coordinate in the last 150 steps, if not the drunk moves, if it has then
# the drunk does not move.

#The function was developed in this file as it was easier to test. Testing was
#done through the print statements which have been commented out. Once the 
#function worked well and did as intended the code was transfered to the
#agentframework for drunks file.
 
import random

lx = []
ly = []

num_list = [10, -10]

x = 150
y = 150

ny = y
nx = x

ly.append(y)

for i in range(10000):
    #print(y)
    if y >=139 and y <= 159:
        y = y + random.choice(num_list)
        #print y
    if random.random() <= 0.5:
        if y <= 10:
           # print(y)
            y = y + 10
            #print(y)
        else:
            ny = y
            ny = ny - (random.randint(1,10))
            for i in ly:
                if i == ny:
                    #print(ny, y)
                    y = y
                    #print(ny, y)
                else:
                    y = ny
                    ly.append(ny)
                    #print(ly)
                    ly = ly[-150:]
                    #print(ly)
                    break
    else:
        if y >= 290:
            #print(y)
            y = y - 10
            #print(y)
        else:
            ny = y
            #print(y, ny)
            ny = ny + (random.randint(1,10))
            for i in ly:
                if i == ny:
                    y = y
                    #print(ly, y, ny)
                    ly = ly[-150:]
                    #print(ly)
                else:
                    y = ny
                    ly.append(ny)
                    #print(ly)
                    ly = ly[-150:]
                    #print(y)
                    break

            
print(ly)

lx.append(x)

for i in range(10000):
    if x >=139 and x <= 159:
        #print(x)
        x = x + random.choice(num_list)
        #print(x)
    if random.random() <= 0.5:
        if x <= 10:
            #print(x)
            x = x + 10
            #print(x)
        else:
            nx = x
            nx = nx - (random.randint(1,10))
            #print(nx)
            for i in lx:
                if i == nx:
                    x = x
                else:
                    x = nx
                    lx.append(nx)
                    lx = lx[-150:]
                    #print(lx, x, nx)
                    break
    else:
        if x >= 290:
            #print(x)
            x = x - 10
            #print(x)
        else:
            nx = x
            nx = nx + (random.randint(1,10))
            #print(nx)
            for i in lx:
                if i == nx:
                    #print(lx)
                    x = x
                    lx = lx[-150:]
                    #print(lx)
                else:
                    x = nx
                    #print(x)
                    lx.append(nx)
                    #print(lx)
                    lx = lx[-150:]
                    #print(lx)
                    break

            
print(lx)