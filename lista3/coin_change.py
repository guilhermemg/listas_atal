
m = []

def __create_matrix(n, k):	
	for i in range(0, len(n)):
		m.append([])
		for j in range(0, k):
			m[i].append(0)

def make_coin_change(n, k):
    if k > n:
       return "k must be <= n"   

    if k == 0:
       return "k must be > 0"
    
    new_n = n + 1
    new_k = k + 1
    
    __create_matrix(new_n, new_k)    

    for i in range(0, new_n):
        for j in range(0, min(i, new_k)):
            if j == 0 or j == i:
                m2[i][j] = 1
            else:
                m2[i][j] = m2[i-1][j-1] + m2[i-1][j]
    
    for l in m2:
        print l

    return m2[n][k-1] 


if __name__ == '__main__':
	values = [ 11, 26 ]
	ds = [ [1, 5, 10, 25, 50] ] # coins values
	
	t = make_coin_change(ds[0], values[0])
	print "t: " + str(t)
	assert t == 4
	
	t2 = make_coin_change(ds[0], values[1])
	print "t2: " + str(t2)
	assert t2 == 13
	
