package algoritmo;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class BigBang {

	private Map<Case, Grafo> map;

	public class Grafo {
		private Map<Vertice, List<Warmhole>> vertices;

		public Grafo() {
			this.vertices = new TreeMap<Vertice, List<Warmhole>>();
		}

		public void addVertice(Integer verticeId, List<Warmhole> warmholes) {
			this.vertices.put(new Vertice(verticeId), warmholes);
		}

		public Map<Vertice, List<Warmhole>> getVertices() {
			return vertices;
		}

	}

	public class Warmhole {
		Vertice starSystemDestination;
		Integer time;

		public Warmhole(Vertice starSystemDestination, Integer time) {
			this.starSystemDestination = starSystemDestination;
			this.time = time;
		}

		public Vertice getDestination() {
			return starSystemDestination;
		}

		public Integer getTime() {
			return time;
		}
	}

	public class Vertice implements Comparable<Vertice> {
		Integer id;
		Integer distance;
		private Integer predecessor;
		private boolean root;

		public Vertice(Integer id) {
			this.id = id;
		}

		public Integer getDistance() {
			return distance;
		}

		public void setDistance(int distance) {
			this.distance = distance;
		}

		public Integer getId() {
			return id;
		}

		public Integer getPredecessor() {
			return predecessor;
		}

		public void setPredecessor(Integer predecessor) {
			this.predecessor = predecessor;
		}

		public boolean isRoot() {
			return root;
		}

		public void setRoot(boolean root) {
			this.root = root;
		}

		@Override
		public int compareTo(Vertice v2) {
			return this.id.compareTo(v2.getId());
		}

	}

	class Case implements Comparable<Case> {
		Integer id;
		Integer n, m;

		public Case(Integer id, Integer n, Integer m) {
			this.id = id;
			this.n = n;
			this.m = m;

		}

		@Override
		public int compareTo(Case c2) {
			return this.id.compareTo(c2.id);
		}
	}

	public class Extrator {

		public Map<Case, Grafo> extract() {
			Map<Case, Grafo> result = new TreeMap<Case, Grafo>();

			Scanner scanner = null;

			scanner = new Scanner(System.in);
			Integer c = Integer.parseInt(scanner.nextLine());
			int c_aux = 1;
			while (c_aux <= c) {
				Grafo grafo = new Grafo();

				String nm = scanner.nextLine();
				Integer n = Integer.parseInt(nm.split(" ")[0]), m = Integer
						.parseInt(nm.split(" ")[1]);
				while (m > 0) {
					String l = scanner.nextLine();
					if (l.equals("")) {
						break;
					}
					String[] line = l.split(" ");
					Integer v1 = Integer.parseInt(line[0]), v2 = Integer
							.parseInt(line[1]);

					Integer time;
					if (v1 == v2) {
						time = 0;
					} else {
						time = Integer.parseInt(line[2]);
					}
					Vertice v = new Vertice(v1);

					if (!grafo.getVertices().containsKey(v)) {
						List<Warmhole> warmholes = new ArrayList<Warmhole>();
						grafo.getVertices().put(new Vertice(v1), warmholes);
					}
					grafo.getVertices().get(new Vertice(v1))
							.add(new Warmhole(new Vertice(v2), time));

					m--;
				}
				result.put(new Case(c_aux, n, m), grafo);
				c_aux++;
			}

			scanner.close();

			return result;

		}
	}

	public BigBang() {
		map = new Extrator().extract();
	}

	public void findBigBang() {
		for (Case c : map.keySet()) {
			Grafo g = map.get(c);
			Map<Vertice, Integer> distance = new TreeMap<Vertice, Integer>();
			Map<Vertice, Vertice> predecessor = new TreeMap<Vertice, Vertice>();

			// Step 1: initialize graph
			for (Vertice vertice : g.getVertices().keySet()) {
				if (vertice.getId() == 0) {
					distance.put(vertice, 0);
				} else {
					distance.put(vertice, Integer.MAX_VALUE);
					predecessor.put(vertice, null);
				}

			}

			// Step 2: relax edges repeatedly
			for (Vertice vertice : g.getVertices().keySet()) {

				for (Warmhole w : g.getVertices().get(vertice)) {
					if (distance.get(vertice) + w.getTime() < distance.get(w
							.getDestination())) {
						distance.put(w.getDestination(), distance.get(vertice)
								+ w.getTime());
						predecessor.put(w.getDestination(), vertice);
					}
				}
			}
			
			boolean possible = false;
			// Step 3: check for negative-weight cycles
			for (Vertice vertice : g.getVertices().keySet()) {

				for (Warmhole w : g.getVertices().get(vertice)) {
					if (distance.get(vertice) + w.getTime() < distance.get(w
							.getDestination())) {
						possible = true;
						break;
					}
				}

			}
			
			if (possible) {
				System.out.println("possible");
			} else {
				System.out.println("not possible");
			}
		}

	}

	public static void main(String[] args) {

		new BigBang().findBigBang();

	}
}
