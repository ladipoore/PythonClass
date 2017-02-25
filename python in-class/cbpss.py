# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:04:40 2017

@author: Oore
"""
"""
This program takes a document showing all the ratings received by an officer
it then returns some basic information about the officer's performance
"""
import statistics
#import numpy as np
filename = input("Enter a filename: ")
file = open(filename,'r')
ratings = file.readlines()
file.close()

# convert to integer
for i in range(len(ratings)):
    ratings[i] = int(ratings[i])

avgr = statistics.mean(ratings)
sdr = statistics.stdev(ratings)

print("Highest Rating: ",max(ratings))
print("Lowest Rating: ",min(ratings))
print("Avergae Rating: %0.4f" %(avgr))


print("# of 1 Ratings: ",str(ratings.count(1)))
print("# of 2 Ratings: ",str(ratings.count(2)))
print("# of 3 Ratings: ",str(ratings.count(3)))
print("# of 4 Ratings: ",str(ratings.count(4)))
print("# of 5 Ratings: ",str(ratings.count(5)))
print("Standard Deviation of Ratings: %0.4f" %(sdr))