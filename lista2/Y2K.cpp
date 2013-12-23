#include <cstdlib>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

// registra superavit ou deficit para os meses, segundo vai sendo achado nas permutacoes de meses
vector<int> meses(generate_n(back_insert_iterator(meses), 12); 

bool verificaPermutacaoValida(vector<int> permutacaoDeMeses, int s ,int d) {
    int ganhoDaPermutacao = accumulate(permutacaoDeMeses.begin(), permutacaoDeMeses.end());
    
    if(ganhoDaPermutacao > 0)
      return false;
    else // houve deficit na permutacao de 5 meses
      return true;
}

int quantidadeDeSs = 0;
int quantidadeDeDs = 5;

void permutaMeses(int s , int d, vector<int> permutacaoDeMeses) {   
      for(int i = 0; i < quantidadeDeSs; i++) {
	    meses.push_back(s);
      }
      for(int j = 0; j < quantidadeDeDs; j++) {
	    meses.push_back(d);
      }
      
      while(next_permutation(permutacaoDeMeses.begin(), permutacaoDeMeses.end())) {
	  if(verificaPermutacaoValida()) {
	      for(int i = I; i < I+5; i++) {
		  meses[i] = permutacaoDeMeses[i];
	      }
	      
	  }
      }
}

int calculaSuperavitAnual(int s, int d) {
      int ganhoAnual = accumulate(meses.begin(), meses.end());
      
      if(ganhoAnual > 0)
	 return ganhoAnual;
      else {
	 if(permutaMeses(s, d))
	     calculaSuperavitAnual(s, d);
	 else {
	     return -1;
	 }
      }
}


int main() {
    // achar um conjunto de 8 permutacoes de 5 meses consecutivos
    // tal que cada permutacao tenha deficit (ganho(permutacao) < 0)
    
    // calcular superavit anual para as 8 permutacoes
    
    int d = 237;
    int s = 59;
    
    int supAnual = calculaSuperavitAnual(d, s);
    
    if(supAnual > 0)
      printf("%d\n", supAnual);
    else
      printf("Deficit\n");
    
    return 0;
}