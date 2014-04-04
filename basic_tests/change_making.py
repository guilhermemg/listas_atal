
m = []

def __create_matrix(d, N):	
	for i in range(0, len(d)):
		m.append([])
		for j in range(0, N):
			m[i].append(0)

def make_change(d, N):
	new_d = [0]
	for coin_val in d:
	    new_d.append(coin_val)
	
	new_N = N+1
	
	#print "new_d: " + str(new_d)
	#print "new_N: " + str(new_N)
	
	__create_matrix(new_d, new_N)
	
	for j in range(1, new_N):  					# C[i,j] = j, if d[i] = 1
		m[1][j] = j
	
	#print "m: " + str(m)
	
	for i in range(2, len(new_d)):   
		for j in range(1, new_N):
			if (j < new_d[i]):            		# C[i,j] = C[i-1, j], if j < d[i]
				m[i][j] = m[i-1][j]
			else: 								# C[i,j] = min( C[i-1, j], C[i, j-d[i]] + 1 )
				m[i][j] = min(m[i-1][j], 1 + m[i][j-new_d[i]])
	
	#for l in m:
	#	print l
	
	return m[len(d)][N]

if __name__ == '__main__':
	values = [ 30, 8 ]
	ds = [ [1, 5, 10, 25, 50], [1, 4, 6] ] # coins values
	
	t = make_change(ds[1], values[1])
	print "t: " + str(t)
	assert t == 2
	
	t2 = make_change(ds[0], values[0])
	print "t2: " + str(t2)
	assert t2 == 2
	
	
