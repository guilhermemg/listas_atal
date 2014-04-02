
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <assert.h>

using namespace std;

vector< vector<int> > m;

void __create_matrix(int n, int W) {
    for (int i = 0; i < n; i++) {
		vector<int> v;
		m.push_back( v );
		for (int j = 0; j < W; j++) {
			m[i].push_back(0);
		}
	}
}

int find_max_value(vector<int> v, vector<int> w, int W) {
    int n = (int) v.size();
	
	__create_matrix(n, W);
	
	for(int i = 1; i < n; i++) {
		for (int j = 1; j < W; j++) {
			if( w[i] > j ) {
				m[i][j] = m[i-1][j];
			}
			else {
				m[i][j] = max(v[i] + m[i-1][j - w[i]], m[i-1][j]);
			}
		}
	}
	
	return m[n-1][W-1];
}

int process_itens(vector<int> v, vector<int> w, vector<int> Ws) {
	//print "v: " + str(v)
    //print "w: " + str(w)
    //print "Ws: " + str(Ws)
    
    vector<int> new_v;
    new_v.push_back(0);
    
    vector<int> new_w;
    new_w.push_back(0);
    
	for(unsigned int i = 0 ; i < v.size(); i++) {
	    //printf("v[%d] : %d\n", i, v[i]);
	    new_v.push_back(v[i]);
	}
	for(unsigned int i = 0 ; i < w.size(); i++) {
	    //printf("w[%d] : %d\n", i, w[i]);    
	    new_w.push_back(w[i]);
	}
    
	//for(unsigned int i = 0 ; i < v.size(); i++) 
	    //printf("new_v[%d] : %d\n", i, new_v[i]);
	//for(unsigned int i = 0 ; i < w.size(); i++) 
	    //printf("new_w[%d] : %d\n", i, new_w[i]);
	
    int s = 0;
    for (unsigned int i = 0; i < Ws.size(); i++) {
		//print "W: " + str(W)
		
		int ans = find_max_value(new_v, new_w, Ws[i]);
		
		s = s + ans;
	}
	
    return s;
}

int main(){
    vector< vector<int> > values;
    int a1[] = {72, 44, 31};
    int a2[] = {64, 85, 52, 99, 39, 54};
    values.push_back( vector<int>( a1, a1 + sizeof(a1)/sizeof(a1[0]) ) );
    values.push_back( vector<int>( a2, a2 + sizeof(a2)/sizeof(a2[0]) ) );
    
	vector< vector<int> > weights;
    int w1[] = {17, 23, 24};
    int w2[] = {26, 22, 4, 18, 13, 9};
    weights.push_back( vector<int>(w1, w1 + sizeof(w1)/sizeof(w1[0])) );
    weights.push_back( vector<int>(w2, w2 + sizeof(w2)/sizeof(w2[0])) );
    
	vector< vector<int> > Ws;
	int ws1[] = {26};
	int ws2[] = {50};
	int ws3[] = {23,20,20,26};
	Ws.push_back( vector<int>( ws1, ws1 + sizeof(ws1)/sizeof(ws1[0])) );
	Ws.push_back( vector<int>( ws2, ws2 + sizeof(ws2)/sizeof(ws2[0])) );
	Ws.push_back( vector<int>( ws3, ws3 + sizeof(ws3)/sizeof(ws3[0])) );
	
	int t1 = process_itens(values[0], weights[0], Ws[0]);
	printf("t1: %d\n", t1);
	assert(t1 == 72);
	printf("----------------------\n");
	
	int t3 = process_itens(values[0], weights[0], Ws[1]);
	printf("t3: %d\n",t3);
	assert(t3 == 116);
	printf("----------------------\n");
	
	int t2 = process_itens(values[1], weights[1], Ws[2]);
	printf("t2: %d\n", t2);
	assert(t2 == 514);
	printf("----------------------\n");
    
    return 0;
}
