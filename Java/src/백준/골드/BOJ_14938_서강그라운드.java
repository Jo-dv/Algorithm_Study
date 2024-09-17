package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_14938_서강그라운드 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, r;
	static int[] t;  // 각 지역의 아이템 수
	static int a, b, l;
	static List<Edge>[] edges;
	static int answer = 0;
	
	static class Edge {
		int dest, cost;

		public Edge(int dest, int cost) {
			this.dest = dest;
			this.cost = cost;
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		t = new int[n + 1];
		st = new StringTokenizer(br.readLine());
				
		for(int i = 1; i <= n; i++)
			t[i] = Integer.parseInt(st.nextToken());
				
		edges = new List[n + 1];
		for(int i = 0; i <= n; i++)
			edges[i] = new ArrayList<>();
		
		for(int i = 1; i <= r; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			l = Integer.parseInt(st.nextToken());
			
			edges[a].add(new Edge(b, l));  // a에서 b로 가는데 l만큼 거리를 가짐
			edges[b].add(new Edge(a, l));
		}
		
		solve();
	}
	
	static void dijkstra(int start) {
		int[] costs = new int [n + 1];
		int items = 0;
		Arrays.fill(costs, Integer.MAX_VALUE);
		costs[start] = 0;
		PriorityQueue<Edge> pq = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);
		pq.add(new Edge(start, costs[start]));
		
		while(!pq.isEmpty()) {
			Edge current = pq.poll();
			
			if(costs[current.dest] < current.cost)
				continue;
			
			for(Edge next: edges[current.dest]) {
				if(next.cost + current.cost < costs[next.dest]) {
					costs[next.dest] = next.cost + current.cost;
					pq.add(new Edge(next.dest, costs[next.dest]));
				}
			}
		}
		
		for(int i = 1; i <= n; i++)
			if(costs[i] <= m)  //  갱신된 거리들에 대해서 탐색 범위에 속하는 지역들만
				items += t[i];
		
		answer = Math.max(answer, items);
	}
	
	static void solve() {
		for(int i = 1; i <= n; i++)
			dijkstra(i);
		
		System.out.println(answer);
	}
}
