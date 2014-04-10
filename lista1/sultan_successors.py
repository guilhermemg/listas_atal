"""
   167 - Sultan Successors Problem
"""

row = []
a = None
b = None
lineCounter = None
tablet_chess = None

def __start_globals(pos, tc):
	global a
	global b
	global lineCounter
	global tablet_chess
	
	a = pos[0] - 1
	b = pos[1] - 1
	lineCounter = 0
	tablet_chess = tc

def place(r, c):
    for prev in range(0, c):
        if row[prev] == r or (abs(row[prev] - r) == abs(prev - c)):
            return False
    return True

def backtrack(c):
    global row
    global a
    global b
    global lineCounter
    global tablet_chess
    
    if (c == 8 and row[b] == a):
        s = 0
        for i in range(0,len(row)):
            s = s + tablet_chess[i][row[i]]

        lineCounter = lineCounter + 1

        auxRow = [row[0] + 1]
        for j in range(1, 8):
            auxRow.append(row[j] + 1)
        
        print "%2d	%s  sum: %d" % (lineCounter, str(auxRow), s)

    for r in range(0, 8):
        if place(r, c):
			#print "row: " + str(row)
			row[c] = r
			backtrack(c + 1)

if __name__ == '__main__':
    tablet = []
    k = 1
    for p in range(0, 8):
		for q in range(0, 8):
			if p % 8 == 0:
			    tablet.append([0 for v in range(0,8)])
			tablet[p][q] = k
			k = k+1
    
    print "tablet: "
    for l in tablet:
		print l
    print ""
	
    row = [0 for i in range(0,8)]
    pos1 = (1,5)
    __start_globals(pos1, tablet)
	
    print("SOLN       COLUMN\n");
    print(" #      1 2 3 4 5 6 7 8\n");
    backtrack(0)
