package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_17472_2 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static int[][] grid;
	static int label = 1;
	static int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static boolean[][] visited;
	static boolean[] visitedPrim;
	static int answer = 0;
	static int v;
	static PriorityQueue<Edge> pq = new PriorityQueue<>((e1, e2) -> e1.cost - e2.cost);
	static ArrayList<ArrayList<Edge>> vertex;  // 어떤 한 정점에서 갈 수 있는 다른 정점(간선 관리)
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		grid = new int[n][m];
		visited = new boolean[n][m];
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++)
				grid[i][j] = Integer.parseInt(st.nextToken()) * -1;
		}
		
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				if(grid[i][j] == -1)
					bfs(i, j); 
		
		v = label - 1;
		vertex = new ArrayList<ArrayList<Edge>>();
		for (int i = 0; i <= v; i++)
			vertex.add(new ArrayList<>());
		visitedPrim = new boolean[v + 1];
		hr();
		vr();
		
		int cnt = 1;
		visitedPrim[1] = true;
		pq.addAll(vertex.get(1));  // 시작 정점에서 갈 수 있는 모든 다른 정점을 담음
		
		while(!pq.isEmpty()) {
			Edge e = pq.poll();
			// 방문 여부 체크해서 방문하지 않았다면 다시 큐에 저장
			if(visitedPrim[e.v]) 
				continue;
			//방문하고 큐에 저장
			visitedPrim[e.v] = true;
			pq.addAll(vertex.get(e.v));
			answer += e.cost;
			cnt++;
			if(cnt == v)
				break;
		}
		if(cnt != v || answer == 0)
			answer = -1;
		
		System.out.println(answer);
		
//		for (int[] i : grid) {
//			System.out.println(Arrays.toString(i));
//		}
	}
	
	static void addEdge(int v1, int v2, int cost) {
		// 뒤져서 중복인 항목을 제거하는 것이 손해가 될 수도 있고 이득이 될 수도 있다.
		boolean same = false;
		
		for (Edge edge : vertex.get(v1)) {  // v1 정점에서 갈 수 있는 다른 정점(간선) 정보 각각
			// 같은 정점을 연결하는 간선이면 최소값으로 갱신
			if(edge.v == v2) {
				same = true;
				edge.cost = Math.min(edge.cost, cost);
				break;
			}
		}
		if(!same)  // 간선 추가
			vertex.get(v1).add(new Edge(v2, cost));
	}
	
	static void hr() {
		for (int i = 0; i < n; i++) {
			int prev = 0;
			int current = 0;
			int v1 = 0;
			int v2 = 0;
			int cost = 0;
			
			for (int j = 0; j < m; j++) {
				current = grid[i][j];
				if(prev == 0 && current != 0) {  // 0에서 0이 아닌 곳으로 이동
					if(v1 == 0)
						v1 = current;
					else {
						// 간선 발생
						v2 = current;
						if(cost > 1) {
							// 간선 추가 v1 -> v2, (v1, v2, cost)
							addEdge(v1, v2, cost);
							addEdge(v2, v1, cost);
						}
						v1 = v2;
						v2 = 0;
						cost = 0;
					}
				}
				else if(v1 != 0 && current == 0)  // 섬에서 시작했는데 아직 바다인 경우
					cost++;
				prev = current;
			}
		}
	}
	
	static void vr() {
		for (int i = 0; i < m; i++) {
			int prev = 0;
			int current = 0;
			int v1 = 0;
			int v2 = 0;
			int cost = 0;
			
			for (int j = 0; j < n; j++) {
				current = grid[j][i];
				if(prev == 0 && current != 0) {  // 0에서 0이 아닌 곳으로 이동
					if(v1 == 0)
						v1 = current;
					else {
						// 간선 발생
						v2 = current;
						if(cost > 1) {
							// 간선 추가 v1 -> v2, (v1, v2, cost)
							addEdge(v1, v2, cost);
							addEdge(v2, v1, cost);
						}
						v1 = v2;
						v2 = 0;
						cost = 0;
					}
				}
				else if(v1 != 0 && current == 0)  // 섬에서 시작했는데 아직 바다인 경우
					cost++;
				prev = current;
			}
		}
	}
	
	static void bfs(int sy, int sx) {
		Queue<Node> q = new ArrayDeque<>();
		q.offer(new Node(sy, sx));
		visited[sy][sx] = true;
		grid[sy][sx] = label;
		
		while(!q.isEmpty()) {
			Node current = q.poll();
			for (int[] d : direction) {
				int my = current.y + d[0];
				int mx = current.x + d[1];
				if(0 <= my && my < n && 0 <= mx && mx < m && !visited[my][mx] && grid[my][mx] == -1) {
					visited[my][mx] = true;
					grid[my][mx] = label;
					q.offer(new Node(my, mx));
				}
			}
		}
		label++;
	}
	
	static class Edge {
		int v, cost;

		public Edge(int v, int cost) {
			this.v = v;
			this.cost = cost;
		}
	}
	
	static class Node {
		int y, x;

		public Node(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}

}
