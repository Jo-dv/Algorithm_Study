package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_2206_벽부수고이동하기 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static int[][] map;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		
		for(int i = 0; i < n; i++) {
			String line = br.readLine();
			for(int j = 0; j < m; j++) 
				map[i][j] = line.charAt(j) - '0';
		}
		
		solve();
	}
	
	static class Node {
		int y, x, cnt, step;

		public Node(int y, int x, int cnt, int step) {
			this.y = y;
			this.x = x;
			this.cnt = cnt;
			this.step = step;
		}
	}
	
	static int bfs() {
		int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		boolean[][][] visited = new boolean[2][n][m];  // 벽을 부술 수 있는 지에 따라 방문 처리를 달리해야 함 -> 벽을 부수고 지나간 곳을 벽을 부수지 않고 지나갈 때 지나갈 수 있게
		Queue<Node> q = new ArrayDeque<>();
		
		visited[1][0][0] = true;
		q.offer(new Node(0, 0, 1, 1));
		
		while(!q.isEmpty()) {
			Node current = q.poll();
			if(current.y == n - 1 && current.x == m - 1)
				return current.step;
			
			for(int[] d: directions) {
				int my = current.y + d[0];
				int mx = current.x + d[1];
				
				if(0 <= my && my < n && 0 <= mx && mx < m && !visited[current.cnt][my][mx]) {
					if(current.cnt == 1 && map[my][mx] == 1)  // 벽을 부술 수 있고, 다음 위치가 벽이라면
						q.offer(new Node(my, mx, 0, current.step + 1));  // 다음 위치가 벽인지 체크를 안 해도 무방하지만 탐색 범위를 좁히기 위해 추가
					else if(map[my][mx] == 0)  // 벽을 안 부순 상태에서(부술 수 있는 횟수가 남아있던 없던 상관없이) 길이라면
						q.offer(new Node(my, mx, current.cnt, current.step + 1));
					visited[current.cnt][my][mx] = true;  // 방문 안한 지역을 돌기 때문에 해당 코드는 반드시 실행
				}
			}
		}
		
		return -1;
	}
	
	static void solve() {
		System.out.println(bfs());
	}
}
