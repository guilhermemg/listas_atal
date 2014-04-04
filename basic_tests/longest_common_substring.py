"""
   Longest Common Substring using Dynamic Programming
"""

def lcs(x, y):
	m = []
	for i in range(0, len(x)):
	   m.append([])
	   for j in range(0, len(y)):
		   m[i].append(0)
	
	for i in range(1, len(x)):
		for j in range(1, len(y)):
			if x[i] == y[j]:
				m[i][j] = 1 + m[i-1][j-1]
			else:
				m[i][j] = max(m[i-1][j], m[i][j-1])
	
	return m[len(x)-1][len(y)-1]

if __name__ == '__main__':
    x = "actb"
    y = "atb"
    print lcs(x, y)
