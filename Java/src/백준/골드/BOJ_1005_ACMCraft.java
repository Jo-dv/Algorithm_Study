package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1005_ACMCraft {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int t;
	static int n, k;
	static int[] d;
	static ArrayList<ArrayList<Integer>> graph;
	static int x, y;
	static int w;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < t; i++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			
			d = new int[n + 1];
			st = new StringTokenizer(br.readLine());
			for(int j = 1; j <= n; j++)
				d[j] = Integer.parseInt(st.nextToken());
			
			graph = new ArrayList<ArrayList<Integer>>();
			for(int j = 0; j <= n; j++)
				graph.add(new ArrayList<>());
			for(int j = 1; j <= k; j++) {
				st = new StringTokenizer(br.readLine());
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());
				graph.get(x).add(y);
			}
			w = Integer.parseInt(br.readLine());	
			solve();
		}
		System.out.println(sb);
	}
	
	static void solve() {
		int[] time = new int[n + 1];
		int[] indgree = new int[n + 1];
		for(int i = 1; i <= n; i++) {  // 진입 차수 계산
			for(int node: graph.get(i))
			indgree[node]++;
		}
		
		Queue<Integer> q = new ArrayDeque<>();
		for(int i = 1; i <= n; i++)
			if(indgree[i] == 0) {
				q.offer(i);
				time[i] = d[i];
			}
		
		while(!q.isEmpty()) {
			int current_building = q.poll();
			
			for(int next_building: graph.get(current_building)) {
				if(time[current_building] + d[next_building] > time[next_building])
					time[next_building] = time[current_building] + d[next_building];
				if(--indgree[next_building] == 0)
					q.add(next_building);
			}
		}
		
		sb.append(time[w]).append("\n");
	}

}
