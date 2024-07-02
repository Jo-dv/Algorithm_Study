package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_17472 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static int[][] grid;
	static int label = 1;
	static int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static boolean[][] visited;
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		grid = new int[n][m];
		visited = new boolean[n][m];
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++) {
				grid[i][j] = Integer.parseInt(st.nextToken());
				grid[i][j] *= -1;
			}
		}
		
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				if(grid[i][j] == -1)
					bfs(i, j); 
		
		for (int[] i : grid) {
			System.out.println(Arrays.toString(i));
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
	
	static class Node {
		int y, x;

		public Node(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}

}
