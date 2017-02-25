# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:15:51 2017

@author: Oore Ladipo
"""

filename = input("Enter a filename: ")
file = open(filename,'r')
count = 0
for line in file:
    inputlist = line.split()
    count += 1
    if count == 1:
        maxtix = float(inputlist[1])
        mintix = float(inputlist[1])
        tottix = 0 + float(inputlist[1])
    else:
        if maxtix < float(inputlist[1]):
            maxtix = float(inputlist[1])
        if mintix > float(inputlist[1]):
            mintix = float(inputlist[1])
        tottix += float(inputlist[1])
    avgtix = tottix/ count

header = 50*"*"+"\n" + "TICKET REPORT".center(50)+"\n" + 50*"*"
main1 = "\nThere are %d tickets in the database.\n\nMaximum Ticket price is $%.2f."%(count,maxtix)
main2 = "\nMinimum Ticket price is $%.2f."%(mintix)
main3 = "\nAverage Ticket Price is $%.2f.\n" %(avgtix)
closer = "\nThank you for using our ticket system!\n\n"+50*"*"
output = header+main1+main2+main3+closer
    

file2 = open ("output.txt", "w")
file2.write(output)
file2.close()


