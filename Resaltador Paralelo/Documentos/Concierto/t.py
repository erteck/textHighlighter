#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:07:58 2020

@author: erick_b
"""
import random
        
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    data = []
    lectures = 0
    for simulation in range(0,N):
        while True:
            lectures += 1
            if random.random() <= aLecture.get_listen_prob() and random.random() <= aLecture.get_sleep_prob() and random.random() <= aLecture.get_fb_prob():
                data.append(lectures)
                lectures = 0
                break
        
    mean, std = get_mean_and_std(data)
    
    return(mean,std*4)

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values,bins=numBins)
    if title != None:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    data = []
    for i in range(0,numTrials):
        results = []
        for k in range(0,numRolls+1):
            results.append(die.roll())
        
        maxroll = 0
        actualroll = 0
        
        for i in range(len(results)-1):
            if results[i] == results[i + 1]:
                actualroll += 1
            else:
                actualroll = 1
            if actualroll > maxroll:
                maxroll = actualroll
        data.append(maxroll)
        
    mean,std = getMeanAndStd(data)
    makeHistogram(data, 10, 'Longest Run', 'frequency')
    return mean
    
print(getAverage(Die([1]), 500, 10000))
    
import numpy as np
import itertools
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    powerset = []
    for i in itertools.product([1,0], repeat = len(choices)):
        powerset.append(np.array(i))
    
    same = []
    similar = []
    
    for option in powerset:
        if sum(option*choices) == total:
            same.append(option)
        elif sum(option*choices) < total:
            similar.append(option)
            
    sum_sames = []
    sum_similar =[]
    if len(same) > 0:
        for element in same:
            sum_sames.append(sum(element))
        return same[sum_sames.index(min(sum_sames))]
        
    else:
        
        for element in similar:
            sum_similar.append(sum(element))
        return similar[sum_similar.index(max(sum_similar))]
   
    
    
    
    
    
    
    
    
    
    
    
    
