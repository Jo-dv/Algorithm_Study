package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_11779_최소비용구하기2 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int m;
	static List<Node>[] graph;
	static int departure, arrival;
	
	static class Node {
		int dest, cost;

		public Node(int dest, int cost) {
			this.dest = dest;
			this.cost = cost;
		}
	}
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		graph = new ArrayList[100000 + 1];  // m + 1로 초기화할 경우 특정 케이스에서 ArrayIndexOutOfBounds 발생
		for(int i = 0; i < 100000 + 1; i++)
			graph[i] = new ArrayList<>();
		
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int d = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			graph[d].add(new Node(a, c));
		}
		st = new StringTokenizer(br.readLine());
		departure = Integer.parseInt(st.nextToken());
		arrival = Integer.parseInt(st.nextToken());
		
		solve();
	}
	
	static int[] dijkstra() {
		int[] total_cost = new int[n + 1];
		int[] tracking = new int[n + 1];
		boolean[] visited = new boolean[n + 1];
		Arrays.fill(total_cost, Integer.MAX_VALUE);
		PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);
		
		pq.add(new Node(departure, 0));
		total_cost[departure] = 0;
		
		while(!pq.isEmpty()) {
			Node current = pq.poll();

			if(visited[current.dest])
				continue;
			
			visited[current.dest] = true;
			
			for(Node next: graph[current.dest])
				if(current.cost + next.cost < total_cost[next.dest]) {
					total_cost[next.dest] = current.cost + next.cost;
					tracking[next.dest] = current.dest;  // 바로 직전 진입 노드를 기록
					pq.add(new Node(next.dest, total_cost[next.dest]));
				}
		}
		System.out.println(total_cost[arrival]);
		
		return tracking;
	}
	
	static void print_path(int[] tracking) {
		List<Integer> path = new ArrayList<>();
        for (int at = arrival; at != 0; at = tracking[at])  // 도착지부터 역추적
            path.add(at);
        
        int len = path.size();
        System.out.println(len);
        for (int i = len - 1; i >= 0; i--)
            System.out.print(path.get(i) + " ");
	}
	
	static void solve() {
		print_path(dijkstra());;
	}
}