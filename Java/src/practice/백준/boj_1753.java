package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class boj_1753 {

	static int V, E, K;
	static List<List<Edge>> adjList = new ArrayList<>();
	static int[] cost;  // -> 다익스트라 구조
	static boolean[] visit;
	static PriorityQueue<Edge> pq = new PriorityQueue<>((e1, e2) -> e1.c - e2.c);
	static StringBuilder sb = new StringBuilder();
	static final int INF = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(br.readLine());
		
		cost = new int[V + 1];
		visit = new boolean[V + 1];
		
		// 인접리스트 초기화
		for(int i = 0; i <= V; i++) {
			adjList.add(new ArrayList<Edge>());
			cost[i] = INF;
		}
		
		// 간선
		for(int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int v1 = Integer.parseInt(st.nextToken());
			int v2 = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			
			// v1 -> v2
			adjList.get(v1).add(new Edge(v2, w));
		}

		// 다익스트라 풀이
		dijkstra();
		
		for(int i = 1; i <= V; i++)
			sb.append(cost[i] == INF ? "INF" : cost[i]).append("\n");
		System.out.println(sb);
	}
	
	static void dijkstra() {
		// 시작 정점
		cost[K] = 0;
		pq.offer(new Edge(K, 0));
		
		while(!pq.isEmpty()) {
			Edge e = pq.poll();  // 꺼낸 간선이 갈 수 있는 정점 고려 -> 이 정점에서 갈 수 있는 다른 정점과의 비용으로 cost 갱신
			if(visit[e.v]) continue;
			visit[e.v] = true;
			
			for (Edge ne : adjList.get(e.v)) {
				if(ne.c + cost[e.v] < cost[ne.v]) {  
					// 아직 방문하지 않은 정점임과 동시에 cost 감소가 가능한 경우: e.v -> ne.v의 비용 cost[e.v]와 cost[ne.v] 비교
					cost[ne.v] = ne.c + cost[e.v];
					pq.offer(new Edge(ne.v, cost[ne.v]));  // Edge 객체 새로 생성
					
//					ne.c = cost[ne.v]; pq.offer(ne);
				}
			}
		}
	}
	
	static class Edge{
		int v, c;
		Edge(int v, int c) {
			this.v = v;
			this.c = c;
		}
	}
}
