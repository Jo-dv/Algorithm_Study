package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_1194 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static char[][] map;
	static boolean[][][] visited;
	static int[] init_pos = new int[2];
	static int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static int answer = -1;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new char[n][m];
		visited = new boolean[64][n][m];
		
		for(int i = 0; i < n; i++) {
			String columns = br.readLine();
			for(int j = 0; j < m; j++) {
				map[i][j] = columns.charAt(j);
				if(map[i][j] == '0') {
					init_pos[0] = i;
					init_pos[1] = j;
				}
			}
		}
		bfs();
		System.out.println(answer);
	}
	// 0은 시작 위치, 1은 탈출구(여러개 존재), #은 통과 불가, 소문자를 얻으면 대문자 통과 가능
	
	static void bfs() {
		int key, y, x;
		y = init_pos[0];
		x = init_pos[1];
		Queue<Node> q = new ArrayDeque<>();
		q.offer(new Node(y, x, 0, 0));  // y, x
		visited[0][y][x] = true;
		map[y][x] = '.';
		
		while(!q.isEmpty()) {
			Node current = q.poll();
			if(map[current.y][current.x] == '1') {
				answer = current.step;
				return;
			}
			for (int[] d : direction) {
				int my = current.y + d[0];
				int mx = current.x + d[1];
				
				if(isValid(current.key, my, mx)) {
					if('a' <= map[my][mx] && map[my][mx] <= 'z') {
						key = current.key | (1 << (map[my][mx] - 'a'));
						q.offer(new Node(my, mx, current.step + 1, key));
						visited[key][my][mx] = true;
					}
					else if('A' <= map[my][mx] && map[my][mx] <= 'Z') {
						if((current.key & (1 << (map[my][mx] - 'A'))) != 0) {
							q.offer(new Node(my, mx, current.step + 1, current.key));
							visited[current.key][my][mx] = true;
						}	
					}
					else {
						q.offer(new Node(my, mx, current.step + 1, current.key));
						visited[current.key][my][mx] = true;
					}
				}
				
			}
		}
	}
	
	static boolean isValid(int key, int y, int x) {
		if(0 <= y && y < n && 0 <= x && x < m && map[y][x] != '#' && !visited[key][y][x])
			return true;
		return false;
	}
	
	static class Node {
		int y, x;
		int step;
		int key;
		
		public Node(int y, int x, int step, int key) {
			this.y = y;
			this.x = x;
			this.step = step;
			this.key = key;
		}
	}

}
