"""
   Topological Sort
"""

def __getAdjs(node, G_e):
    adjs = []
    for e in G_e:
        if e[0] == node and e[0] not in adjs:
            adjs.append(e[1])
        #elif e[1] == node and e[1] not in adjs:
        #    adjs.append(e[0])

    return adjs

color = None
pi = None
d = None  # time of discovery
f = None  # time of finalization
time = None
found = None

linked_list = None  # to make topological sort

def __start_globals(G_v):
    global color
    global pi
    global d
    global f
    global time
    global found
    
    global linked_list
    
    color = ['WHITE' for v in G_v]
    pi = [None for v in G_v]
    d = [None for v in G_v]
    f = [None for v in G_v]
    time = 0
    found = False
    linked_list = []

def dfs(node2f, G):
    global color
    global pi
    global d
    global f
    global time
    global found
	
    G_v = G[0]
    G_e = G[1]
    
    __start_globals(G_v)
	
    for i in range(0, len(G_v)):
		if color[i] == 'WHITE':
			__dfs_visit(G_v[i], node2f, G_e)
	
    return found

def __dfs_visit(node, node2f, G_e):
	global color
	global pi
	global d
	global f
	global time
	global found
	
	global linked_list
	
	if node == node2f:
		found = True
	
	color[node] = 'GRAY'
	time = time + 1
	
	d[node] = time
	
	print "d= " + str(d)
	
	adj_vs = __getAdjs(node, G_e)
	print "node = %d adjs: " % node,str(adj_vs)
	
	for vl in adj_vs:
		if color[vl] == 'WHITE':
			pi[vl] = node
			__dfs_visit(vl, node2f, G_e)
	
	color[node] = 'BLACK'
	time = time + 1
	f[node] = time
	
	print "f: " + str(f)
	
	linked_list.append(node)


def topological_sort(G):
    for v in G[1]:
		dfs(v, G)
    
    tmp = linked_list[:]
    top_sort = [linked_list.pop() for v in tmp]
    
    print "top_sort: " + str(top_sort)
    
    return top_sort


if __name__ == '__main__':
   #G_e1 = ((8, 9), (3, 7), (1, 4), (7, 8), (0, 5), (5, 2), (3, 8), (2, 9), (0, 6), (4, 9), (2, 6), (6, 4))
   #G_v1 = (0,1,2,3,4,5,6,7,8,9)
   #G1 = (G_v1, G_e1)    
   
   #topological_sort(G1)
   
   print "====================="
   
   G_e2 = ( (0,1), (0,3), (1,2), (3,1), (4,2), (4,5) )
   G_v2 = ( 0, 1, 2, 3, 4, 5 )
   G2 = (G_v2, G_e2)
   
   a2 = topological_sort(G2)
   assert str(a2) == str([4, 5, 0, 3, 1, 2]);
   
