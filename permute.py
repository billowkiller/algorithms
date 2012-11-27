A = [1,2,3,4,5]

def heapPermute(n):
	if n == 1:
	    print A
	else:
	    for i in range(n):
		heapPermute(n-1)
		if n%2 == 1:
		    temp = A[0]
		    A[0] = A[n-1]
		    A[n-1] = temp
		else:
		    temp = A[i]
		    A[i] = A[n-1]
		    A[n-1] = temp

heapPermute(5)
