package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_1967_트리의지름 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int p, c, w;
	static List<List<Node>> graph = new ArrayList<>();
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		for(int i = 0; i <= n; i++)
			graph.add(new ArrayList<>());
		
		for(int i = 0; i < n - 1; i++) {
			st = new StringTokenizer(br.readLine());
			p = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			
			graph.get(p).add(new Node(c, w));
			graph.get(c).add(new Node(p, w));
		}
		
		solve();
	}
	
	static void dfs(int start, int weight, int[] visited) {
		for(Node node: graph.get(start)) {
			if(visited[node.c] == -1) {
				int next_weight = weight + node.w;
				visited[node.c] = next_weight;
				dfs(node.c, next_weight, visited);
			}
		}
	}
	
	static int find_max(int[] visited) {
		return Arrays.stream(visited).max().getAsInt();
	}
	
	static int[] init_array(int idx) {
		int[] visited = new int[n + 1];
		Arrays.fill(visited, -1);
		visited[idx] = 0;  //  시작하는 노드의 가중치는 없음(=0)
		
		return visited;
	}
	
	static void solve() {
		int[] visited = init_array(n);  // 어느 정점에서 시작하든 상관없음 -> 사이클이 형성되어있지 않은 무방향 그래프이기 때문에 무조건 경로가 하나만 존재
		dfs(n, 0, visited);  // 임의의 정점에서 도착한 노드 중 거리가 가장 먼 노드는 지름의 끝이라고 볼 수 있음
		
		int idx = -1;
		int max_num = find_max(visited);  // 1차 탐색이 끝나면 임의의 정점에서 가장 멀리 떨어진 노드 탐색
		for(int i = 0; i < n + 1; i++)
			if(visited[i] == max_num) {  // 노드의 인덱스 탐색
				idx = i;
				break;
			}
		
		visited = init_array(idx);  // 찾아낸 끝점에서 다시 가장 먼 노드를 찾으면 끝과 끝을 찾을 수 있음
		dfs(idx, 0, visited);
		
		System.out.println(find_max(visited));
	}
	
	static class Node {
		int c, w;
		
		Node(int c, int w) {
			this.c = c;
			this.w = w;
		}
	}
}
