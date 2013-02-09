import pygame, sys, os, csv, math

def mil2mm(mil):
	return mil * 0.00254

xZero = 0
yZero = 0
rowOne = 0
x = 0
y = 0

furosFile  = csv.reader(open('furos', 'rb'), delimiter='Y')
for furo in furosFile:
	if(furo[0][0] == 'X'):
		
		x = int(furo[0][1:])
		y = int(furo[1])
		if rowOne == 1:
			xZero = x
			yZero = y
			rowOne = 0
		else:
			x = mil2mm(x - xZero)
			y = mil2mm(y - yZero)
			print "X" + str(x) + " Y" + str(y)
			
		print "Z-2.5"
		print "Z3"
		
print "Z10"
print "X0 Y0"