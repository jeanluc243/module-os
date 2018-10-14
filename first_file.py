#A small scripts that shows the first file of any folder
#from os import *
#from sys import *
import os
import sys
#folder=sys.argv[1]
current_path=os.getcwd()
folders=os.listdir()
sizes=list()
all_files=list()
for folder in folders:
	if folder=='first_file.py':
		continue
	os.chdir(folder)
	all_files=os.listdir()
	sizes+=[len(all_files)]
	print(sizes)
	os.chdir(current_path)
print(folders)
print("hello guys")
max_index=0
for i in range(len(sizes)-1):
	if sizes[i]<sizes[i+1]:
		max_index=i+1
print("The biggest file has got ",sizes[max_index]," files")
#os.chdir(folder)
#way=getcwd()
#all_files=os.listdir()
#size_file=len(all_files)
#print(size_file)

