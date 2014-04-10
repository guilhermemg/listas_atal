import sys

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

def bfs(node):
    found = False
    color = [None for v in G_v]
    pi = [0 for v in G_v]
    d = [0 for v in G_v]
    
    print color
    print pi
    print d    
 
    for v in G_v:
        color[v] = 'WHITE'
        pi[v] = None
        d[v] = -1
   
    color[0] = 'GRAY'
    pi[0] = None
    d[0] = 0
    Q = []
    Q.append(G_v[0])

    while(len(Q) > 0):
		#if Q[0] == node:
		#	return True
		
		print "Q: " + str(Q)
		v = Q.pop(0)
		print "v: " + str(v)
		
		adj_vs = __getAdjs(v)
		print "adjs: " + str(adj_vs)
		
		for aux_v in adj_vs:
			if color[aux_v] == 'WHITE':
				color[aux_v] = 'GRAY'
				pi[aux_v] = v
				d[aux_v] = d[v] + 1
				Q.append(aux_v)
			color[v] = 'BLACK'
		
		print "color: " + str(color)
		print "pi: " + str(pi)
		print "d: " + str(d)
		
		if v == node:
			found = True
			break
    
    return d

def node_too_far(node, ttl):
	ans = bfs(node)
	result = []
	for i in range(0, len(ans)):
		if ans[i] <= ttl:
			result.append(i)
	
	return result

if __name__ == '__main__':
   ttl1 = 1
   n1 = 3
   a1 = node_too_far(n1, ttl1)
   print "a1: " + str(a1)
   assert(str(a1) == str([0, 5, 6]) )
   
   ttl1 = 1
   n1 = 3
   a1 = node_too_far(n1, ttl1)
   print "a1: " + str(a1)
   assert(str(a1) == str([0, 5, 6]) )
   
   ttl1 = 1
   n1 = 3
   a1 = node_too_far(n1, ttl1)
   print "a1: " + str(a1)
   assert(str(a1) == str([0, 5, 6]) )

