package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_17144_다시풀기 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int r, c, t;
	static int[][] grid;
	static int[][] origin;
	static Queue<Node> q;
	static int[][] cleaner;
	static int pos = 0;
	static int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static int answer = 0;;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		t = Integer.parseInt(st.nextToken());
		grid = new int[r][c];
		origin = new int[r][c];
		cleaner = new int[2][2];
		q = new ArrayDeque<>();
		for(int i = 0; i < r; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < c; j++) {
				grid[i][j] = Integer.parseInt(st.nextToken());
				if(grid[i][j] > 0) q.offer(new Node(i, j, grid[i][j]));
				if(grid[i][j] == -1) {
					cleaner[pos][0] = i;
					cleaner[pos][0] = j;
					pos++;
				}
			}
			origin[i] = grid[i].clone();
		}
		
		for(int i = 0; i < t; i++) {
			spread();
		}
		
		for (int[] i : grid) {
			System.out.println(Arrays.toString(i));
		}
	}
	
	static void spread() {	
		while (!q.isEmpty()) {
			int cnt = 0;
			Node current = q.poll();
			for (int[] d : direction) {
				int my = current.y + d[0];
				int mx = current.x + d[1];
				if(grid[my][mx] < 5)
					continue;
				if(0 <= my && my < r && 0 <= mx && mx < c && grid[my][mx] != -1) {
					grid[my][mx] += (current.dust / 5);
					cnt++;
				}
			}
			grid[current.y][current.x] -= (current.dust / 5) * cnt;
		}
	}
	
	static class Node {
		int y, x, dust;

		public Node(int y, int x, int dust) {
			this.y = y;
			this.x = x;
			this.dust = dust;
		}
	}

}
