"""
   DFS - Deep First Search
"""

G_e = [(8, 9), (3, 7), (1, 4), (7, 8), (0, 5), (5, 2), (3, 8), (2, 9), (0, 6), (4, 9), (2, 6), (6, 4)]
G_v = [0,1,2,3,4,5,6,7,8,9]

def __getAdjs(node):
    adjs = []
    for e in G_e:
        if e[0] == node and e[0] not in adjs:
            adjs.append(e[1])
        elif e[1] == node and e[1] not in adjs:
            adjs.append(e[0])

    return adjs

color = None
pi = None
d = None  # time of discovery
f = None  # time of finalization
time = None
found = None

def __start_globals():
    global color
    global pi
    global d
    global f
    global time
    global found
    
    color = ['WHITE' for v in G_v]
    pi = [None for v in G_v]
    d = [None for v in G_v]
    f = [None for v in G_v]
    time = 0
    found = False

def dfs(node2f):
    global color
    global pi
    global d
    global f
    global time
    global found
	
    __start_globals()
	
    for i in range(0, len(G_v)):
		color[i] = 'WHITE'
		pi[i] = None
	
    #print "start color: " + str(color)
    #print "start pi: " + str(pi)
	
    for i in range(0, len(G_v)):
		if color[i] == 'WHITE':
			__dfs_visit(G_v[i], node2f)
	
    return found

def __dfs_visit(node, node2f):
	global color
	global pi
	global d
	global f
	global time
	global found
	
	if node == node2f:
		found = True
	
	color[node] = 'GRAY'
	time = time + 1
	
	d[node] = time
	
	adj_vs = __getAdjs(node)
	print "adjs: " + str(adj_vs)
	
	for vl in adj_vs:
		if color[vl] == 'WHITE':
			pi[vl] = node
			__dfs_visit(vl, node2f)
	
	color[node] = 'BLACK'
	time = time + 1
	f[node] = time


if __name__ == '__main__':
    a1 = dfs(10)
    print "a1: " + str(a1)
    assert a1 == False
    
    a2 = dfs(2)
    print "a2: " + str(a2)
    assert a2 == True
    
    a3 = dfs(23)
    print "a3: " + str(a3)
    assert a3 == False
    
    
    
