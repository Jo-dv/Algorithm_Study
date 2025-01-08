package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_15681_트리와쿼리 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, r, q;
	static int u, v;
	static ArrayList<Integer>[] graph;
	static int[] queries;
	static int[] node;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		q = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList[n + 1];
		for(int i = 1; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}
		
		
		for(int i = 1; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			graph[u].add(v);
			graph[v].add(u);
		}

		queries = new int[q];
		for(int i = 0; i < q; i++) {
			queries[i] = Integer.parseInt(br.readLine());
		}
		node = new int[n + 1];
		
		solve();

	}
	
	static void dfs(int current, boolean[] visited) {
		node[current] = 1;
		visited[current] = true;
		
		for(int next: graph[current]) {
			if(!visited[next]) {
				dfs(next, visited);
				node[current] += node[next];
			}
		}
	}

	static void solve() {
		boolean[] visited = new boolean[n + 1]; 
		dfs(r, visited);
		for(int query: queries) {
			sb.append(node[query]).append("\n");
		}
		
		System.out.println(sb);
	}
}
