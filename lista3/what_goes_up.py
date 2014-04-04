

import sys

def what_goes_up(x):
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
					print "include el: " + str(x[i])
			
			print "------"		
			print "m= " + str(m)
			print "mx: " + str(mx)
	
	#i = m.index(mx)
	#for j in range(0, i+1):
	#	if x[j] < x[i]:
	#		print x[j]
	#print x[i]
	
	return mx


if __name__ == '__main__':
    #x1 = [-7, 10, 9, 2, 3, 8, 8, 1]
    #a1 = what_goes_up(x1)
    #print "a1: " + str(a1)
    #assert a1 == 4
    
    #print "========================="
    
    x2 = [1, 3, 2, 4, 3, 5, 4, 6]
    a2 = what_goes_up(x2)
    print "a2: " + str(a2)
    assert a2 == 5
