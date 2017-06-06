import sys
#import csv
#import os

'''Change this accordingly depending on how your data is'''
f=open(sys.argv[1], "r")
string = ""

for txt in f:
	string += str(txt)

string.split(' ')
print(string)



'''
with open(sys.argv[1]) as csvfile:
	reader = csv.DictReader(csvfile)
'''

