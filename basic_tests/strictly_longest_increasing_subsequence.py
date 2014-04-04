"""
   The Strictly Longest Increasingly Subsequence
"""

import sys

m = []
def __create_matrix(x):
	for i in range(0, len(x)):
		m.append(1)

def slis(x):
	__create_matrix(x)
	
	n = len(x)
	mx = -sys.maxint
	
	for i in range(1, n):
		for j in range(0, i):
			if x[i] > x[j] and m[i] < m[j] + 1:
				m[i] = m[j] + 1
				if mx < m[i]:
					mx = m[i]
	
	return mx


if __name__ == '__main__':
	x1 = [-7, 10, 9, 2, 3, 8, 8, 1]
	a1 = slis(x1)
	print a1
	assert a1 == 4
	
	x2 = [1, 3, 2, 4, 3, 5, 4, 6]
	a2 = slis(x2)
	print a2
	assert a2 == 5
