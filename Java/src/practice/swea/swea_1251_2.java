package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class swea_1251_2 {
	static int t, n;
	static long answer;
	
	static int[][] island;  // 0: x, 1: y
	static List<List<Edge>> vertex;
	static PriorityQueue<Edge> pq = new PriorityQueue<>((e1, e2) -> Long.compare(e1.c, e2.c));
	static boolean[] visit;
	static double e;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		for(int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			island = new int[n][2];
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i = 0; i < n; i++)
				island[i][0] = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i < n; i++)
				island[i][1] = Integer.parseInt(st.nextToken());
			
			e = Double.parseDouble(br.readLine());
			
			vertex = new ArrayList<>();
			for(int i = 0; i < n; i++) {
				vertex.add(new ArrayList<Edge>());
			}
			
			for(int v1 = 0; v1 < n- 1; v1++) {
				for(int v2 = v1 + 1; v2 < n; v2++) {
					
					Edge edge1 = new Edge(v2, distance(island[v1][0], island[v2][0], island[v1][1], island[v2][1]));
					Edge edge2 = new Edge(v1, distance(island[v1][0], island[v2][0], island[v1][1], island[v2][1]));
					vertex.get(v1).add(edge1);
					vertex.get(v2).add(edge2);
				}
			}
			
			// prim
			visit = new boolean[n];
			pq.clear();
			
			answer = 0;
			int cnt = 1;
			visit[0] = true;
			pq.addAll(vertex.get(0));
			while(!pq.isEmpty()) {
				Edge edge = pq.poll();
				if(visit[edge.v]) continue;
				visit[edge.v] = true;
				answer += edge.c;
				cnt++;
				
				if(cnt == n) break;
				for (Edge e : vertex.get(edge.v)) {
					if(visit[e.v]) continue;
					pq.offer(e);
				}
			}

			
			sb.append("#").append(tc).append(" ").append(Math.round(answer * e)).append("\n");
		}
		System.out.println(sb);

	}
	
	static long distance(int x1, int x2, int y1, int y2) {
		return (long) (Math.pow(x1-x2, 2) + Math.pow(y1-y2, 2));
	}
	
	// 어떤 정점으로부터 선탣해서 다른 정점으로 이동할 수 있는 간선 정보, v : 선택하면 
	static class Edge {
		int v;
		long c;
		
		Edge(int v, long c) {
			this.v = v;
			this.c = c;
		}
	}

}
