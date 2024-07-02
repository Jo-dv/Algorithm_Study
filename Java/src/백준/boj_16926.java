package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_16926 {

	static int n, m, r;
	static int[][] grid;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		
		grid = new int[n][m];
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++)
				grid[i][j] = Integer.parseInt(st.nextToken());
		}
		
		// 풀이
		for(int i = 0; i < r; i++) {
			rotate();
		}
		
		// 출력
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++)
				sb.append(grid[i][j]).append(" ");
			sb.append("\n");
		}
		System.out.println(sb);
	}
	
	static void rotate() {
		int sy = 0, ey = n - 1;
		int sx = 0, ex = m - 1;
		
		while(true) {
			// end check
			if(ey - sy < 1 || ex - sx < 1)
				return;
			
			// 회전
			// 왼쪽 위 값 -> temp
			int temp = grid[sy][sx];
			
			// 상단 -> 좌 방향 이동
			for (int i = sx; i < ex; i++) grid[sy][i] = grid[sy][i + 1];
			
			// 우측 -> 상 방향 이동
			for (int i = sy; i < ey; i++) grid[i][ex] = grid[i + 1][ex];
			
			// 하단 -> 우 방향 이동
			for (int i = ex; i > sx; i--) grid[ey][i] = grid[ey][i - 1];
			
			// 좌측 -> 하 방향 이동
			for (int i = ey; i > sy; i--) grid[i][sx] = grid[i - 1][sx];
			grid[sy + 1][sx] = temp;
			
			// 가운데로 sy, sx, ey, ex 보정 -> 다음 사각형 좌표로
			sy += 1;
			sx += 1;
			ey -= 1;
			ex -= 1;
		}
	}
}
