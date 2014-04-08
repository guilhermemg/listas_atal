package algoritmo;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

class Main {

	private Map<Caso, Grafo> map;

	class Grafo {
		Map<String, Vertice> vertices;

		public Grafo() {
			this.vertices = new TreeMap<String, Vertice>();
		}

		public void addVertice(Integer verticeId, String drinkName) {
			this.vertices.put(drinkName, new Vertice(verticeId, drinkName));
		}
		
		public Map<String, Vertice> getVertices() {
			return vertices;
		}
		
	}

	class Aresta {
		Vertice drink1, drink2;

		public Aresta(Vertice drink1, Vertice drink2) {
			this.drink1 = drink1;
			this.drink2 = drink2;
		}

		public Vertice getDrink1() {
			return drink1;
		}

		public Vertice getDrink2() {
			return drink2;
		}
	}

	enum Cor { CINZA, BRANCO, PRETO}
	class Vertice implements Comparable<Vertice>{
		
		Integer id;
		List<Vertice> arestas;
		
		String drinkName;
		Integer cinzaTime, 
				pretoTime;
		Cor cor;
		Vertice pai;

		public Vertice(Integer id, String drinkName) {
			this.id = id;
			this.drinkName = drinkName;
			this.cinzaTime = 0;
			this.pretoTime = 0;
			this.cor = Cor.BRANCO;
			this.pai = null;
			this.arestas = new LinkedList<Vertice>();
		}

		public void addAresta(Vertice v) {
			this.arestas.add(v);

		}
		
		@Override
		public String toString() {
			return "[" + this.drinkName + ": time="+ pretoTime + "]";
		}

		@Override
		public int compareTo(Vertice v2) {
			
			return this.cinzaTime.compareTo(v2.cinzaTime);
		}
	}

	class Caso implements Comparable<Caso> {
		Integer id;

		public Caso(Integer id) {
			this.id = id;
		}

		@Override
		public int compareTo(Caso c2) {
			return this.id.compareTo(c2.id);
		}
	}

	class Extrator {

		public Map<Caso, Grafo> extract() {
			Map<Caso, Grafo> result = new TreeMap<Caso, Grafo>();

			Scanner scanner = null;

			scanner = new Scanner(System.in);
			
			int case_id = 1;
			String stringN = scanner.nextLine();
			Integer N = 0;
			
			while (!stringN.equals("")) {
				
				N = Integer.parseInt(stringN);

				Grafo grafo = new Grafo();

				for (int i = 0; i < N; i++) {
					
					String drinkName = scanner.nextLine();
					
					grafo.addVertice(i, drinkName);
				}
				
				
				Integer M = Integer.parseInt(scanner.nextLine());
				
				for (int i = 0; i < M; i++) {
					String line = scanner.nextLine();
					String drinkName1 = line.split(" ")[0],
						   drinkName2 = line.split(" ")[1];
					
					
					
					grafo.getVertices().get(drinkName1).addAresta(grafo.getVertices().get(drinkName2));
				}
				
				
				result.put(new Caso(case_id), grafo);
				case_id++;
				
				System.out.println("");
				
				stringN = scanner.nextLine();
				
			}
			
			scanner.close();
			
			return result;
		}
	}

	Main() {
		map = new Extrator().extract();
	}

	void Beverages() {
		for (Caso caso: map.keySet()) {
			List<String> topologicalDrinks = topologicalSort(map.get(caso));
			String sortedDrinks = topologicalDrinks.get(0);
			for (int i = 1; i < topologicalDrinks.size(); i++) {
				sortedDrinks += " " + topologicalDrinks.get(i);
			} 
				
			System.out.println("Case #" + caso.id + ": Dilbert should drink beverages in this order: " + sortedDrinks + "\n");
		}
		
	}

	private List<String> topologicalSort(Grafo grafo) {
		List<String> result = new LinkedList<String>();
		for (Vertice v : DFS(grafo)) {
			result.add(v.toString());
		}
		return result;
	}

	private List<Vertice> DFS(Grafo g) {
		//Já iniciamos a cor e o pai de cada vertice na instanciacao.
		List<Vertice> result = new LinkedList<Vertice>();
		int time = 0;
		
		for (Vertice v : g.getVertices().values()) {
			if (v.cor == Cor.BRANCO) {
				DFS_Visit(v, time, result);
			}
		}
		Collections.sort(result);
		return result;
		
	}

	private void DFS_Visit(Vertice v, Integer time, List<Vertice> result) {
		v.cor = Cor.CINZA;
		time++;
		v.cinzaTime = time;
		for (Vertice v2 : v.arestas) {
			if (v2.cor == Cor.BRANCO) {
				v2.pai = v;
				DFS_Visit(v2, time, result);
			}
		}
		v.cor = Cor.PRETO;
		time++;
		v.pretoTime = time;
		result.add(0, v);
		
	}

	public static void main(String[] args) {
		new Main().Beverages();
	}
}
