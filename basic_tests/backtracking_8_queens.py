"""
   8-Queens Problem
"""

row = []
a = None
b = None
lineCounter = None

def __start_globals(pos):
	global a
	global b
	global lineCounter
	
	a = pos[0] - 1
	b = pos[1] - 1
	lineCounter = 0

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
    
    if (c == 8 and row[b] == a):
        lineCounter = lineCounter + 1

        auxRow = [row[0] + 1]
        for j in range(1, 8):
            auxRow.append(row[j] + 1)
        print "%2d	%s" % (lineCounter, str(auxRow))

    for r in range(0, 8):
        if place(r, c):
			#print "row: " + str(row)
			row[c] = r
			backtrack(c + 1)

if __name__ == '__main__':
    row = [0 for i in range(0,8)]
    pos1 = (1,1)
    __start_globals(pos1)
    
    print("SOLN       COLUMN\n");
    print(" #      1 2 3 4 5 6 7 8\n");
    backtrack(0)
