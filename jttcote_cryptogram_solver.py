#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:24:07 2017

@author: Carlson

--* Program to solve: 
   'Jules Verne's: Journey to the Center of the Earth' 
    Cryptogram *--
"""
#import re

mystring = """
m.rnlls esreuel seecJde
sgtssmf unteief niedrke
kt,samn atrateS Saodrrn
emtnaeI nuaect  rrilSa 
Atvaar  .nscrc  ieaabs 
ccdrmi  eeutul  frantu 
dt,iac  oseibo  KediiY
"""

print(mystring)

step = 8
mylist = list(mystring)
newlist = []
    
start = 0
for j in range(step):
    for i in range(j,len(mystring),step):
        newlist.append(mylist[i])
        
revstring = (newlist[::-1])
concat = "".join(revstring)
solution = concat.strip()
#solution = re.compile('\s+').sub('',concat)

print('')
print('Solution = ' + solution)

