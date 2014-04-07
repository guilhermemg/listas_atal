#include <cstdio>
#include <cstdlib>
#include <assert.h>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

struct Node {
    int id;
    string color;
    int pi_id;
    int d;  // time of discovery
    int f;  // time of finalization

    vector<int> adjs_nodes_ids;
    
    Node(int identi) {
		this->id = identi;
	}
	
	void set_adjs_nodes(vector<int> adjs) {
		adjs_nodes_ids = adjs;
	}
};

vector<Node> top_sort;
vector<Node> dag;
bool found;
int t;

void __start_globals(vector<Node> G) {
    for(size_t i = 0; i < G.size(); i++) {
		G[i].color = "WHITE";
		G[i].pi_id = -1;
		G[i].d = -1;
		G[i].f = -1;
    }
    
    t = 0;
    found = false;
    dag = G;
}

void __print_dag() {
	printf("--------------------------------\n");
	for(size_t i = 0; i < dag.size(); i++) {
		printf("Node[%d]: ", dag[i].id);
		for(size_t j = 0; j < dag[i].adjs_nodes_ids.size(); j++) {
			printf("%d ", dag[dag[i].adjs_nodes_ids[j]].id);
		}
		printf("\n");
		printf("\td = %d | f = %d | pi_id = %d\n", dag[i].d, dag[i].f, dag[i].pi_id);
	}
}

void __dfs_visit(int node_id, int node2f_id) {
	if (node_id == node2f_id)
		found = true;
	
	dag[node_id].color = "GRAY";
	t++;
	dag[node_id].d = t;
	
	vector<int> adj_nodes_ids = dag[node_id].adjs_nodes_ids;
	
	for (size_t vli = 0; vli < adj_nodes_ids.size(); vli++) {
		if ( dag[adj_nodes_ids[vli]].color.compare("WHITE") == 0 ) {
			dag[adj_nodes_ids[vli]].pi_id = node_id;
			__dfs_visit(adj_nodes_ids[vli], node2f_id);
		}
	}
	
	dag[node_id].color = "BLACK";
	t++;
	dag[node_id].f = t;
	
	__print_dag();

	top_sort.push_back(dag[node_id]);
}

bool dfs(int node2f_id) {
    for(size_t i = 0; i < dag.size(); i++) {
		if((dag[i].color).compare("WHITE") == 0) {
			__dfs_visit(dag[i].id, node2f_id);
		}
	}
	
    return found;
}

void topological_sort(vector<Node> dag) {
    top_sort.clear();
    
    __start_globals(dag);
	__print_dag();
    
    for(size_t i = 0; i < dag.size(); i++) {
		bool b = dfs(dag[i].id);
		printf("dfs[%d]: %s\n", dag[i].id, b? "true" : "false");
	}
	
	printf("top_sort.size: %d\n", (int)top_sort.size());
	
	reverse(top_sort.begin(), top_sort.end());
	
	for(size_t i = 0; i < top_sort.size(); i++) {
		printf("Node: %d\n", top_sort[i].id);
	}
}

int main() {
    vector<Node> dag;
    
    Node n0(0), n1(1), n2(2), n3(3), n4(4), n5(5);
    
    vector<int> adjs0;
    adjs0.push_back(1);
    adjs0.push_back(3);
    n0.set_adjs_nodes(adjs0);
    
    vector<int> adjs1;
    adjs1.push_back(2);
    n1.set_adjs_nodes(adjs1);
    
    vector<int> adjs3;
    adjs3.push_back(1);
    adjs3.push_back(2);
    n3.set_adjs_nodes(adjs3);
    
    vector<int> adjs4;
    adjs4.push_back(2);
    adjs4.push_back(5);
    n4.set_adjs_nodes(adjs4);
    
    dag.push_back(n0);
    dag.push_back(n1);
    dag.push_back(n2);
    dag.push_back(n3);
    dag.push_back(n4);
    dag.push_back(n5);
    
    topological_sort(dag);
    
    assert(top_sort[0].id == 4);
    assert(top_sort[1].id == 5);
    assert(top_sort[2].id == 0);
    assert(top_sort[3].id == 3);
    assert(top_sort[4].id == 1);
    assert(top_sort[5].id == 2);
    
    return 0;
}
