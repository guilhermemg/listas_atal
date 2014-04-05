#include <cstdio>
#include <cstdlib>
#include <stack>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

struct Node {
    int id;
    vector<Node> adjs_nodes;
    //string color;
    //Node pi;
    //int d;  // time of discovery
    //int f;  // time of finalization
    
    Node(int identi) {
		this->id = identi;
	}
	
	void set_adjs_nodes(vector<Node> adjs) {
		adjs_nodes = adjs;
	}
};

stack<Node> top_sort;

vector<string> color;
vector<Node> pi;
vector<int> d;  // time of discovery
vector<int> f;  // time of finalization
int t;            // time
bool found;

void __start_globals(vector<Node> dag) {
    for(size_t i = 0; i < dag.size(); i++) {
		color.push_back("WHITE");
		pi.push_back(Node(-1));
		d.push_back(-1);
		f.push_back(-1);
    }
    
    t = 0;
    found = false;
    //while(!top_sort.empty()) {
    //    top_sort.pop();
	//}
}

void __dfs_visit(Node node, Node node2f) {
	if (node.id == node2f.id)
		found = true;
	
	/*printf("colors -----------\n");
	for(size_t i = 0; i < color.size(); i++) {
	    printf("color[%d]: %s\n", i, color[i].c_str());
	}
	printf("colors -----------\n");
	*/
	
	color[node.id] = "GRAY";
	t++;
	d[node.id] = t;
	
	//printf("Node[%d]:\n", node.id);
	
	vector<Node> adj_nodes = node.adjs_nodes;
	/*for(size_t i = 0; i < adj_nodes.size(); i++) {
		printf("adj_node: %d | ", adj_nodes[i].id);
	}
	printf("\n");
	*/
	
	for (size_t vli = 0; vli < adj_nodes.size(); vli++) {
		if ( color[vli].compare("WHITE") == 0 ) {
			pi[vli] = node;
			__dfs_visit(adj_nodes[vli], node2f);
		}
	}
	
	/*
	printf("colors -----------\n");
	for(size_t i = 0; i < color.size(); i++) {
	    printf("color[%d]: %s\n", i, color[i].c_str());
	}
	printf("colors -----------\n");
	*/
	
	color[node.id] = "BLACK";
	t++;
	f[node.id] = t;
	
	//printf("f -------------- f\n");
	//print "f: " + str(f);
	//for(size_t i = 0 ; i < f.size(); i++) {
		//printf("f: %d\n", f[i]);
	//}
	//printf("f -------------- f\n");

	top_sort.push(node);
}

bool dfs(Node node2f, vector<Node> G) {
    __start_globals(G);
	
    for(size_t i = 0; i  < G.size(); i++) {
		if(color[i].compare("WHITE") == 0) {
			__dfs_visit(G[i], node2f);
		}
	}
	
    return found;
}

int topological_sort(vector<Node> dag) {
    for(size_t i = 0; i < dag.size(); i++) {
		bool b = dfs(dag[i], dag);
		printf("dfs[%d]: %s\n", dag[i].id, b? "true" : "false");
	}
	
	printf("top_sort.size: %d\n", (int)top_sort.size());
	
	while(!top_sort.empty()) {
		Node n = top_sort.top();
		top_sort.pop();
		printf("Node: %d\n", n.id);
	}
	
	return 0;
}

void __print_dag(vector<Node> g) {
	
	for(size_t i = 0; i < g.size(); i++) {
		printf("Node[%d]\n", g[i].id);
		for(size_t j = 0; j < g[i].adjs_nodes.size(); j++) {
			printf("adjs: %d ", g[i].adjs_nodes[j].id);
		}
		printf("\n");
	}
}

int main() {
    vector<Node> dag;
    
    Node n0(0), n1(1), n2(2), n3(3), n4(4), n5(5);
    
    vector<Node> adjs0;
    adjs0.push_back(n1);
    adjs0.push_back(n3);
    n0.set_adjs_nodes(adjs0);
    
    vector<Node> adjs1;
    adjs1.push_back(n2);
    n1.set_adjs_nodes(adjs1);
    
    vector<Node> adjs3;
    adjs3.push_back(n1);
    adjs3.push_back(n2);
    n3.set_adjs_nodes(adjs3);
    
    vector<Node> adjs4;
    adjs4.push_back(n2);
    adjs4.push_back(n5);
    n4.set_adjs_nodes(adjs4);
    
    dag.push_back(n0);
    dag.push_back(n1);
    dag.push_back(n2);
    dag.push_back(n3);
    dag.push_back(n4);
    dag.push_back(n5);
    
    __print_dag(dag);
    
    topological_sort(dag);
    
    return 0;
}
