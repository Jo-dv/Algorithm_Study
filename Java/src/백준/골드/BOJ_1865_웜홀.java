package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_1865_웜홀 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int tc;
	static int n, m, w;
	static int s, e, t;
	static List<Edge> edges;
	static StringBuilder sb = new StringBuilder();
	
	static class Edge {
		int start, end, time;
		
		Edge(int start, int end, int time) {
			this.start = start;
			this.end = end;
			this.time = time;
		}
	}
	
	public static void main(String[] args) throws IOException {
		tc = Integer.parseInt(br.readLine());
		
		while(tc-- > 0) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());  // 노드의 수
			m = Integer.parseInt(st.nextToken());  // 양수 간선의 수
			w = Integer.parseInt(st.nextToken());  // 음수 간선의 수
			
			edges = new ArrayList<>();
			
			for(int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				s = Integer.parseInt(st.nextToken());
				e = Integer.parseInt(st.nextToken());
				t = Integer.parseInt(st.nextToken());
				
				edges.add(new Edge(s, e, t));
				edges.add(new Edge(e, s, t));
			}
			
			for(int i = 0; i < w; i++) {
				st = new StringTokenizer(br.readLine());
				s = Integer.parseInt(st.nextToken());
				e = Integer.parseInt(st.nextToken());
				t = -Integer.parseInt(st.nextToken());
				
				edges.add(new Edge(s, e, t));
			}
			
			solve();
		}
		
		System.out.println(sb);
	}
	
	static boolean bf(int start) {
		int[] cost = new int[n + 1];
		Arrays.fill(cost, Integer.MAX_VALUE);
		cost[start] = 0;
		
		for(int i = 1; i <= n; i++) {
			boolean update = false;
			for(Edge current: edges) {
				if(cost[current.start] != Integer.MAX_VALUE && cost[current.end] > cost[current.start] + current.time) {  // 현재 도달할 수 있고 최소로 갱신가능하다면
					cost[current.end] = cost[current.start] + current.time;
					update = true;
					if(i == n)
						return true;
					// 최단 경로 특성상 갱신을 진행하다보면 특정 값에 수렴하는데, 음수 가중치가 있을경우 무한히 수렴하므로 모든 정점에 대해 검사했을 때도 갱신이 일어나면 사이클이 발생하는 것
				}
			}
			
			if(!update)  // 더 이상 갱신이 일어나지 않으면 종료
				break;
		}
		
		return false;
	}
	
	static void solve() {
		boolean flag = false;
		
		for(int i = 1; i <= n; i++)
			if(bf(i)) {  // 사이클이 발생하는 정점 탐색
				flag = true;
				break;
			}
		
		sb.append(flag ? "YES" : "NO").append("\n");
	}
}
