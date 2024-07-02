package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_9205 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int t;
	static int n;
	static Node home, pentaport;
	static Node[] location;
	static HashSet<Node> set = new HashSet<>();
	
	public static void main(String[] args) throws IOException {
		// 상근이네 출발, 맥주 한 박스 들고감(20개)
		// 50미터당 한 병씩
		// 맥주는 20병을 넘을 수 없음
		// 집, 편의점(n개), 펜타포트 순으로 좌표가 주어짐
		// 좌표는 (x, y)
		 t = Integer.parseInt(br.readLine());
		 for(int tc = 0; tc < t; tc++) {
			 n = Integer.parseInt(br.readLine());
			 st = new StringTokenizer(br.readLine());
			 int x = Integer.parseInt(st.nextToken());
			 int y = Integer.parseInt(st.nextToken());
			 location = new Node[n];
			 home = new Node(x, y);
			 
			 for(int i = 0; i < n; i++) {
				 st = new StringTokenizer(br.readLine());
				 x = Integer.parseInt(st.nextToken());
				 y = Integer.parseInt(st.nextToken());
				 location[i] = new Node(x, y);
			 }
			 st = new StringTokenizer(br.readLine());
			 x = Integer.parseInt(st.nextToken());
			 y = Integer.parseInt(st.nextToken());
			 pentaport = new Node(x, y);
			 sb.append(solve() ? "happy" : "sad").append("\n");
		 }
		 System.out.println(sb);
	}
	
	static int get_distance(int x1, int x2, int y1, int y2) {
		return Math.abs(x1 - x2) + Math.abs(y1 - y2);
	}
	
	static boolean solve() {
		Queue<Node> q = new ArrayDeque<>();
		q.offer(home);
		
		while(!q.isEmpty()) {
			Node current = q.poll();
			if(get_distance(current.x, pentaport.x, current.y, pentaport.y) <= 1000)
				return true;
			for (Node node : location) {
				if(get_distance(current.x, node.x, current.y, node.y) <= 1000 && !set.contains(node)) {
					q.offer(node);
					set.add(node);
				}
			}
		}
		return false;
	}
	
	static class Node {
		int x, y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}
