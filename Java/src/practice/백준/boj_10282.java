package practice.boj;

import java.io.*;
import java.util.*;

public class boj_10282 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int t;
	static int n, d, c;
	static int a, b, s;
	static ArrayList<Computer>[] graph;

	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < t; i++) {  // 그래프 초기화
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());  // 컴퓨터 수
			d = Integer.parseInt(st.nextToken());  // 의존성 수
			c = Integer.parseInt(st.nextToken());  // 해킹당한 컴퓨터
			
			graph = new ArrayList[n+1];
			for(int j = 1; j <= n; j++)
				graph[j] = new ArrayList<>();
			
			for(int j = 0; j < d; j++) {
				st = new StringTokenizer(br.readLine());
				a = Integer.parseInt(st.nextToken());  // 컴퓨터 a가
				b = Integer.parseInt(st.nextToken());  // 컴퓨터 b를 의존하면
				s = Integer.parseInt(st.nextToken());  // 컴퓨터 b가 감염됐을 때, a는 s초 후에 감염
				
				graph[b].add(new Computer(a, s));
			}
			solve(c);
		}
		System.out.println(sb);
	}
	
	static void solve(int first) {
		PriorityQueue<Computer> pq = new PriorityQueue<>((o1, o2) -> o1.time - o2.time);
		int dist[] = new int[n+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[first] = 0;
		pq.add(new Computer(first, dist[first]));
		
		int infection = 0;
		int total_time = 0;
		
		while(!pq.isEmpty()) {
			Computer current = pq.poll();
			
			for (Computer next : graph[current.no]) {
				if(current.time + next.time < dist[next.no]) {
					dist[next.no] = current.time + next.time;
					pq.add(new Computer(next.no, dist[next.no]));
				}
			}
		}
		
		for(int i = 1; i <= n; i++) {
			if(dist[i] != Integer.MAX_VALUE ) {
				infection++;
				total_time = Math.max(total_time, dist[i]);  // 총 걸린 시간은 노드 중 가장 큰 시간을 소요하는 노드의 시간이다. -> 모든 노드를 돌고 마지막으로 해당 노드를 돌기 때문
			}
		}
		sb.append(infection).append(" ").append(total_time).append("\n");
	}
	
	static class Computer {
		int no, time;

		public Computer(int no, int time) {
			this.no = no;
			this.time = time;
		}
	}
}
