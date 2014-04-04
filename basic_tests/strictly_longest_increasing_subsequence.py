"""
   The Strictly Longest Increasingly Subsequence
"""

import sys

"""
def slis(x):
	m = []
	for i in range(0, len(x)):
		m.append(1)
	
	n = len(x)
	mx = -sys.maxint
	
	for i in range(1, n):
		for j in range(0, i):
			if x[i] > x[j] and m[i] < m[j] + 1:
				m[i] = m[j] + 1
				if mx < m[i]:
					mx = m[i]
					
			#print "m= " + str(m)
			#print "mx: " + str(mx)
	
	return mx
"""

def lis(a):
	lis_vec = []
	
	p = [0 for el in a]
	
	if len(a) == 0:
		return
	
	lis_vec.append(0)
	
	for i in range(1, len(a)):
		# If next element a[i] is greater than last element of current
		# longest subsequence a[lis_vec.back()], just push it at back of "lis_vec" and continue
		if (a[lis_vec[len(lis_vec)-1]] < a[i]):
			p[i] = lis_vec[len(lis_vec)-1]
			lis_vec.append(i)
			continue;
		
		# Binary search to find the smallest element referenced by b which is just bigger than a[i]
        # Note : Binary search is performed on b (and not a). Size of b is always <=k 
        #        and hence contributes O(log k) to complexity.    
		v = len(lis_vec)-1
		for u in range(0, v):
			c = (u + v) / 2
			if a[lis_vec[c]] < a[i]:
				u=c+1 
			else:
				v=c
 
        # Update lis_vec if new value is smaller then previously referenced value 
		if (a[i] < a[lis_vec[u]]):
			if (u > 0):
				p[i] = lis_vec[u-1]
			lis_vec[u] = i
	
	for u in range(len(lis_vec), 0):
		v = lis_vec.back()
		lis_vec[u] = v;
		v = p[v]
	
	print "lis_vec: " + str(lis_vec)	
	return lis_vec

if __name__ == '__main__':
	x1 = [-7, 10, 9, 2, 3, 8, 8, 1]
	a1 = lis(x1)
	#print "a1: " + str(a1)
		
	for i in a1:
		print x1[i]
	
	assert len(a1) == 4
	
	print "============================"
	
	x2 = [1, 3, 2, 4, 3, 5, 4, 6]
	a2 = lis(x2)
	#print "a2: " + str(a2)
	
	for i in a2:
		print x2[i]
	
	assert len(a2) == 5
	
	print "============================"
	
	x3 = [1, 9, 3, 8, 11, 4, 5, 6, 4, 19, 7, 1, 7]
	a3 = lis(x3)
	#print "a3: " + str(a3)
	
	for i in a3:
		print x3[i]
	
	assert len(a3) == 6
