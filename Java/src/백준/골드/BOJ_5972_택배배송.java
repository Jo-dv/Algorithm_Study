package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_5972_택배배송 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static int a, b, c;
	static List<Edge>[] edges; 
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		edges = new ArrayList[n + 1];
		for(int i = 1; i <= n; i++)
			edges[i] = new ArrayList<>();
		
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			
			edges[a].add(new Edge(b, c));
			edges[b].add(new Edge(a, c));
			
		}
		
		solve();

	}
	
	static void solve() {
		int[] cost = new int[n + 1];
		Arrays.fill(cost, Integer.MAX_VALUE);
		PriorityQueue<Edge> pq = new PriorityQueue<Edge>((o1, o2) -> o1.c - o2.c);
		
		cost[1] = 0;
		pq.add(new Edge(1, 0));
		
		while(!pq.isEmpty()) {
			Edge current = pq.poll();
			
			if(cost[current.b] < current.c)
				continue;
			
			for (Edge next: edges[current.b]) {
				if(current.c + next.c < cost[next.b]) {
					cost[next.b] = current.c + next.c;
					pq.add(new Edge(next.b, cost[next.b]));
				}
			}
		}
		
		System.out.println(cost[n]);
	}
	
	static class Edge {
		int b, c;
		
		Edge(int b, int c) {
			this.b = b;
			this.c = c;
		}
	}
}
