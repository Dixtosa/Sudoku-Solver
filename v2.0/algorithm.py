#!/usr/bin/python

# Author: Dixtosa
# Language: Python 2
# Date started: doh very early 

test = [
    [0,0,9,  0,5,0,  0,0,0],
    [3,7,0,  6,0,4,  0,9,0],
    [5,0,4,  2,0,8,  0,0,3],
	                 
    [6,0,7,  0,0,0,  0,0,5],
    [0,2,0,  5,0,3,  0,8,0],
    [9,0,0,  0,0,0,  3,0,4],
	                 
    [2,0,0,  7,0,1,  6,0,9],
    [0,9,0,  4,0,2,  0,5,1],
    [0,0,0,  0,6,0,  4,0,0]
	]

class MethodError:
	pass
class LogicalError:
	pass

def getH(matrix, h):
	return matrix[h]
def getV(matrix, v):
	return [row[v] for row in matrix]
def getBox(matrix, h, v):
	h = h / 3 * 3
	v = v / 3 * 3
	return [matrix[h + i][v + j] for i in range(3) for j in range(3)]
def isCorrect(matrix):
	for h in range(9):
		for v in range(9):
			restrictions = set (getH(matrix, h) + getV(matrix, v) + getBox(matrix, h, v))
			All = set(range(1, 10))
			All -= restrictions
			if len(All) != 1:
				return False
	return True

def solve(matrix):
	working = True
	while working:
		working = False
		for h in range(9):
			for v in range(9):
				if matrix[h][v] == 0:
					restrictions = set (getH(matrix, h) + getV(matrix, v) + getBox(matrix, h, v))
					All = set(range(1, 10))
					All -= restrictions
					if len(All) == 1:
						matrix[h][v] = list(All)[0]
						working = True
	for row in matrix:
		if row.count(0) > 0:
			print "This method fails here xD"
			raise MethodError
	
	if not isCorrect(matrix):		
		print "Successful"
		print "\n".join([str(row) for row in matrix])
		return matrix
	else:
		print "Code sucks..."
		raise LogicalError

if __name__ == "__main__":
	solve(test)