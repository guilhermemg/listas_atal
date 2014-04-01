
m = []
def __create_matrix(n, W):
	for i in range(0, n):
		m.append([])
		for j in range(0, W):
			m[i].append(0)


def find_max_value(v, w, W, itens):
	print "v: " + str(v)
	print "w: " + str(w)
	print "W: " + str(W)
	
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
				x = new_v[i] + m[i-1][j - new_w[i]]
				y = m[i-1][j]
				mxy = -1
				if x > y:
					mxy = x
					itens[i] = 1
				else:
					mxy = y
				
				m[i][j] = mxy
	
	print "itens: " + str(itens)
	
	return (m[len(v)][W], itens)

def process_itens(v, w, Ws): 
    # itens = available itens
    
    itens = [0 for i in range(0, len(v)+1)]
    
    Ws.sort()
    
    vals = v
    ws = w
    s = 0
    for W in Ws:
		ans = find_max_value(vals, ws, W, itens)
		s = s + ans[0]
		for i in range(0, len(ans[1])):
			if i == 1:
				vals.pop(i)
				ws.pop(i)
	
    return s
	

if __name__ == '__main__':
	values =  [[72, 44, 31], [64, 85, 52, 99, 39, 54]]
	weights = [[17, 23, 24], [26, 22, 4, 18, 13, 9]]
	Ws = [[26], [50], [23,20,20,26]]
	
	t1 = process_itens(values[0], weights[0], Ws[0])
	print "t1: " + str(t1)
	assert t1 == 72
	print "----------------------"
	
	t3 = process_itens(values[0], weights[0], Ws[1])
	print "t3: " + str(t3)
	assert t3 == 116
	print "----------------------"
	
	t2 = process_itens(values[1], weights[1], Ws[1])
	print "t2: " + str(t2)
	assert t2 == 514
	print "----------------------"
	
