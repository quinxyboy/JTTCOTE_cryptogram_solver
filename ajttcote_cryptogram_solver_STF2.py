#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:24:07 2017

@author: Carlson

--* Program to solve: 
   'Jules Verne's: Journey to the Center of the Earth' 
    Cryptogram *--
"""

from nltk import word_tokenize
from urllib import request

#set url to book text 
url = "https://www.gutenberg.org/files/18857/18857.txt"

#open url
response = request.urlopen(url)

#read book text into a raw string
raw = response.read().decode('utf8')
print(raw[:75])

# tokenise the string into separate words into a list
tokens = word_tokenize(raw)

# get index of starting word in cryptogram
start = tokens.index('mm.rnlls')

# gets crpytogram words and reformats to correct syntax
words = tokens[start:start+25]

#strip first m from first word in the list using slicing
words[0] = words[0][1:]

#join the words that were separates by punctuation
words[20:23] = [''.join(words[20:23])]
words[6:9] = [''.join(words[6:9])]
# fix incorrect word in text
words[1]= words[1]= words[1][:3]+'e'+ words[1][3:]

## add a spacing character to end of 6 letter words (to make 7)
tmp=[]
for word in words:
    if len(word) < 7:
        tmp.append(word+'_')
    else:
        tmp.append(word)
        
words = tmp
# solver for cryptogram part 1 
newlist = []    
step = 7
for j in range(step):
    for i,word in enumerate (words):
        newlist.append(words[i][j])
         
# solver for cryptogram part 2 - reverse text        
revstring = (newlist[::-1])

# concatonate string
concat = "".join(revstring)

# strip spacing 'underscores'
solution = concat.strip('_')

#print solution
print('')
print('Solution = ' + solution)

