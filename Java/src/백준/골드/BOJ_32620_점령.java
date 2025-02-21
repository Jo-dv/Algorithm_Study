package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_32620_점령 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, r;
	static int[] a;
	static int[] b;
	static int u, v;
	static ArrayList<Node>[] graph;
	
	static class Node {
		int num, require, acquire;

		public Node(int num, int require, int acquire) {
			super();
			this.num = num;
			this.require = require;
			this.acquire = acquire;
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		
		a = new int[n + 1];
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i <= n; i++) {
			a[i] = Integer.parseInt(st.nextToken());
		}
		
		b = new int[n + 1];
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i <= n ; i++) {
			b[i] = Integer.parseInt(st.nextToken());
		}
		
		graph = new ArrayList[n + 1];
		for(int i = 1; i <= n; i++) {
			graph[i] = (new ArrayList<Node>());
		}
		
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			graph[u].add(new Node(v, a[v], b[v]));
			graph[v].add(new Node(u, a[u], b[u]));
		}
		
		
		solve();
	}
	
	static void solve() {
		long current_energy = 0;  // 각 노드에서 얻을 수 있는 최대 기력은 10억 -> 3번만 누적되면 int 범위 초과
		boolean[] visited = new boolean[n + 1];
		PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.require - o2.require);  // 필요한 기력이 작은 순으로
		pq.add(new Node(r, a[r], b[r]));
		
		while(!pq.isEmpty()) {
			Node current = pq.poll();
			if(visited[current.num]) {
				continue;
			}
			
			if(!visited[current.num] && current_energy >= current.require) {  // 아직 정복되지 않았고, 취할 수 있는 노드라면 -> 해당 조건 때문에 초기화시 r을 방문처리 하지 않음
				visited[current.num] = true;  // 정복
				current_energy += current.acquire;  // 기력 취함
				
				for(Node next: graph[current.num]) {  // 정복한 노드와 인접한 노드를 탐색 범위에 추가
					pq.add(next);
				}
			}
		}
		
		System.out.println(current_energy);
	}
 }
