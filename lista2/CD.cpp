#include <cstdlib>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

vector<int> solucao;
vector<int> faixas;
int N;
int numFaixas;

bool isValid(vector<int> solution) {		
	for(unsigned int i = 0; i < solution.size()-1; i++){
		if(solution[i] == solution[solution.size()-1]) {
			return false;
		}
	}
	return accumulate(solution.begin(), solution.end(), 0) <= N;
}

void ocupafita(vector<int> parcial) {
	int sum_of_elems_parcial = accumulate(parcial.begin(), parcial.end(), 0);
	int sum_of_elems_solucao = accumulate(solucao.begin(), solucao.end(), 0);
	
	if(sum_of_elems_parcial > sum_of_elems_solucao){
		solucao.clear();
		solucao.insert(solucao.end(), parcial.begin(), parcial.end());
	}
	
	for(unsigned int i = 0 ; i < faixas.size(); i++) {
		vector<int> a = parcial;
		a.push_back(faixas[i]);
		if(isValid(a)){
			ocupafita(a);
		}
	}	
}

int main() {
// 	N = 45;
// 	
// 	faixas.push_back(4);
// 	faixas.push_back(10);
// 	faixas.push_back(44);
// 	faixas.push_back(43);
// 	faixas.push_back(12);
// 	faixas.push_back(9);
// 	faixas.push_back(8);
// 	faixas.push_back(2);
	
	while(scanf("%d %d", &N, &numFaixas)) {
// 	    int flag = ;
	    
	    printf("N: %d\n", N);
	    printf("numFaixas: %d\n", numFaixas);
	    
// 	    if(flag == 0) break;
	    
	    int f;
	    for(int i = 0; i < numFaixas; i++) {
		scanf("%d", &f);
		faixas.push_back(f);
		printf("faixa lida: %d\n", faixas[i]);
	    }
	}
	
	//vector<int> x;
	//ocupafita(x);
	
	printf("faixas.size(): %d\n", faixas.size());
	
	for(unsigned int i = 0; i < solucao.size(); i++) {
		printf("solucao: %d\n", solucao[i]);
	}
	
	return 0;
}

