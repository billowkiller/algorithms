#!/usr/bin/env python

D = ((0,10,20,30,40,50),\
	(12,0,18,30,25,21),\
	(23,19,0,5,10,15),\
	(34,32,4,0,8,16),\
	(45,27,11,10,0,18),\
	(56,22,16,20,12,0))

def convert1(V):
	output = 0
	for each in V:
		output += 2**each
	return output

def convert2(output):
	V = []
	for i in range(5,-1,-1):
		if output >= 2**i:
			V.append(i)
			output -= 2**i
	return V

def tsp(n):
	tmp = []
	T = [[0 for x in range(2**n)] for y in range(6)]
	for i in range(0,n):
		T[i][0] = D[i][0]
		
	for j in range(1,2**(n)-1):
		for i in range(1,n):
			V = convert2(j)
			if 0 in V:
				T[i][j] = T[i][j-1]
				continue
			if i not in V:
				for k in V:
					V_temp = V[:]
					V_temp.remove(k)
					tmp.append(D[i][k] + T[k][convert1(V_temp)])
				T[i][j] = min(tmp)
				tmp = []

	V = [1,2,3,4,5]
	for k in range(1,n):
		V_temp = V[:]
		V_temp.remove(k)
		tmp.append(D[0][k] + T[k][convert1(V_temp)])

	print min(tmp)

if __name__ == '__main__':
	tsp(6)
