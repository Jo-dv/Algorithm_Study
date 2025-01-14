package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class BOJ_17129_윌리암슨수액빨이딱따구리가정보섬에올라온이유 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static char[][] map;
	
	static class Node {
		int y, x, step;
		
		public Node(int y, int x, int step) {
			this.y = y;
			this.x = x;
			this.step = step;
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new char[n][m];
		
		for(int i = 0; i < n; i++) {
			String line = br.readLine();
			for(int j = 0; j < m; j++) {
				map[i][j] = line.charAt(j);
			}
		}
		
		solve();
	}
	
	static Node find_start() {
		Node node = null;
		
		loop1:
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(map[i][j] == '2') {
					node = new Node(i, j, 0);
					break loop1;
				}
			}
		}
		
		return node;
	}
	
	static void search(Node start) {
		int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		boolean[][] visited = new boolean[n][m];
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(map[i][j] == '1') {
					visited[i][j] = true;
				}
			}
		}
		
		ArrayDeque<Node> pq = new ArrayDeque<>();
		pq.add(start);
		visited[start.y][start.x] = true;
		
		while(!pq.isEmpty()) {
			Node current = pq.pop();
			if(map[current.y][current.x] == '3' || map[current.y][current.x] == '4' || map[current.y][current.x] == '5') {
				System.out.println("TAK");
				System.out.println(current.step);
				return;
			}
			
			for(int[] d: directions) {
				int my = current.y + d[0];
				int mx = current.x + d[1];
				
				if(0 <= my && my < n && 0 <= mx && mx < m && !visited[my][mx]) {
					pq.add(new Node(my, mx, current.step + 1));
					visited[my][mx] = true;
				}
			}
		}
		
		System.out.println("NIE");
	}
	
	static void solve() {
		Node start = find_start();
		search(start);
	}
}
