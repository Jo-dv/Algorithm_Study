package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class BOJ_16933_벽부수고이동하기3 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, k;
	static char[][] map;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		map = new char[n][m];
		
		for(int i = 0; i < n; i++) {
			String line = br.readLine();
			for(int j = 0; j < m; j++)
				map[i][j] = line.charAt(j);
		}
		solve();
	}
	
	static void solve() {
		int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		boolean[][][] visited = new boolean[k + 1][n][m];
		ArrayDeque<Node> q = new ArrayDeque<>();
		q.add(new Node(1, 0, 0, k, true));
		visited[k][0][0] = true;
		
		while(!q.isEmpty()) {
			Node current = q.poll();
			if(current.y == n - 1 && current.x == m - 1) {
				System.out.println(current.step);
				return;
			}
			
			for(int[] d: directions) {
				int my = current.y + d[0];
				int mx = current.x + d[1];
				
				if(0 <= my && my < n && 0 <= mx && mx < m) {
					if(map[my][mx] == '1' && current.cnt > 0 && !visited[current.cnt - 1][my][mx]) {  // 벽을 부술 수 있는 경우
						if(current.day) {  // 낮일때만
							visited[current.cnt - 1][my][mx] = true;
							q.add(new Node(current.step + 1, my, mx, current.cnt - 1, !current.day));
						}
						else  // 벽을 부술 수 있는데 낮이 아니라면 부술 수 없으므로 대기
							q.add(new Node(current.step + 1, current.y, current.x, current.cnt, !current.day));
					} if(map[my][mx] == '0' && !visited[current.cnt][my][mx]) {  // 벽을 안 부숴도 되는 경우
						visited[current.cnt][my][mx] = true;
						q.add(new Node(current.step + 1, my, mx, current.cnt, !current.day));
					}
				}
			}
		}
		System.out.println(-1);
	}
	
	static class Node {
		int step, y, x, cnt;
		boolean day;

		public Node(int step, int y, int x, int cnt, boolean day) {
			this.step = step;
			this.y = y;
			this.x = x;
			this.cnt = cnt;
			this.day = day;
		}
	}
}
