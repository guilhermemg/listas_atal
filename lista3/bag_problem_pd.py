
m = []
def __create_matrix(n, W):
	for i in range(0, n):
		m.append([])
		for j in range(0, W):
			m[i].append(0)


def find_max_value(v, w, W):
	new_v = [0]
	new_w = [0]
	
	for vl in v:
		new_v.append(vl)
	
	for wl in w:
		new_w.append(wl)
		
	print "new_v: " + str(new_v)
	print "new_w: " + str(new_w)
	
	new_n = len(new_v)
	new_W = W + 1
	
	__create_matrix(new_n, new_W)
	
	for i in range(1, new_n):
		for j in range(1, new_W):
			if( new_w[i] > j ):
				m[i][j] = m[i-1][j]
			else:
				m[i][j] = max(new_v[i] + m[i-1][j - new_w[i]], m[i-1][j])
			
	return m[len(v)][W]

if __name__ == '__main__':
	values = [12, 10, 20, 15]
	weights = [2, 1, 3, 2]
	W = 5
	
	t = find_max_value(values, weights, W)
	
	assert t == 37
    
