import sys

m = {0 : 0, 1 : 1}

def fib(n):
    if not m.has_key(n):
        m[n] = fib(n-1) + fib(n-2)
    return m[n]

m2 = []
def bin_coef(n, k):
    if k > n:
       return "k must be <= n"   

    if k == 0:
       return "k must be > 0"

    for i in range(0,n+1):
        m2.append([])
        for j in range(0,k+1):
            m2[i].append(0) 

    for i in range(0, n+1):
        for j in range(0, min(i,k+1)):
            if j == 0 or j == i:
                m2[i][j] = 1
            else:
                m2[i][j] = m2[i-1][j-1] + m2[i-1][j]
    
    for l in m2:
        print l

    return m2[n][k-1] 

if __name__ == '__main__':
   if sys.argv[1] == 'fib':
       print fib(int(sys.argv[2]))
   elif sys.argv[1] == 'bin_coef':
       print bin_coef(int(sys.argv[2]), int(sys.argv[3]))
