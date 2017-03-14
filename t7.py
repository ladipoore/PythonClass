"""
Version 1.7
This version has the chunking being completed by estimating the number of lines. 
This is based on some analysis done with the sample data, I took 15 randomly selected samples of 25 lines each and their average size was 1019  
Based on this, I can interpolate the number of lines within a larger file.
Will make a normality test that does all this and more.
#import logging? log texts easier to read and ******
Profiling
"""
#Packages required for program
from mpi4py import MPI
from itertools import islice
from datetime import datetime
#from memory_profiler import profile

#Custom functions used in program
#Chunking function
#@profile
def chunkit(filename,numproc):
	import os
	size = os.path.getsize(file)
	chunksize = ((size//1019)*25)//(numproc -1)
	return(chunksize)

#Cleaning function
#removes negative prices and volumes then rewrites datetime
#@profile
def cleanone(datain):
	import re
	#using a set for output to eliminate duplicates by default
	dataout= set()
	dataformat = re.compile(r"^[0-9:]{9}[0-5][0-9][:0-9]{3}[:0-9]{3}[\.0-9]{7}[,0-9]{4,5}[\.0-9]{3}[,0-9]{5,7}$")
	for line in datain:
		if re.match(dataformat,line):
			dataout.add(str(line))
		else:
			filenoise.write(str(line))
	return(dataout)

def returntime (starttime, endtime):
    return (endtime - starttime)

#Necessary variables for program execution
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
file = "big.txt"
chunk = chunkit(file,nprocs)

#file opening
with open('dirty.txt','w'):pass
filenoise = open('dirty.txt','a')


#Program starts
st = datetime.now()
if rank == 0:
	with open(file)as f:
		i =1
		while True and i < nprocs:
			next10k = list(islice(f,chunk))
			comm.send(next10k, dest=i, tag=11)
			print("Message BLOCK sent to ",i)
			i+=1
elif rank ==1:
	data = comm.recv(source=0, tag = 11)
	print("Message received BLOCK at: ", rank)
	data = cleanone(data)
else:
	data = comm.recv(source=0, tag = 11)
	print("Message received BLOCK at: ", rank)
	data = cleanone(data)
end = datetime.now()
print("The entire program takes ",returntime(st,end))
#fileout.close()
filenoise.close()