package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_17070 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[][] arr;
	static int[][][] memo; // [이동 방향][y][x]
	// [0][y][x] -> 대각
	// [1][y][x] -> 가로
	// [2][y][x] -> 세로

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		arr = new int[n + 1][n + 1];
		memo = new int[3][n + 1][n + 1];
		
		for(int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 1; j <= n; j++)
				arr[i][j] = Integer.parseInt(st.nextToken());
		}
		memo[1][1][2] = 1;  // 초기 파이프
		
		// 현재 위치에서 대각선으로, 가로로, 세로로 이동하는 값을 dp로 계산
		for(int y = 1; y <= n; y++) {
			for(int x = 2; x <= n; x++) {
				// 대각선 memo[0]
				if(y < n && x < n && arr[y + 1][x + 1] == 0 && arr[y][x + 1] == 0 && arr[y + 1][x] == 0) {
					memo[0][y + 1][x + 1] += (memo[0][y][x] + memo[1][y][x] + memo[2][y][x]);
					// 대각선 상태에서, 대각선 이동(유지)이 이루어질 수 있음, 가로 이동(회전), 세로 이동(회전)
				}
				// 가로 memo[1]
				if(x < n && arr[y][x + 1] == 0) {
					memo[1][y][x + 1] += (memo[0][y][x] + memo[1][y][x]);
					// 가로 상태에서, 대각선 이동(회전), 가로 이동(유지)이 이루어질 수 있음
				}
				// 세로 memo[2]
				if(y < n && arr[y + 1][x] == 0) {
					memo[2][y + 1][x] += (memo[0][y][x] + memo[2][y][x]);
					// 세로 상태에서, 대각선 이동(회전), 세로 이동(유지)이 이루어질 수 있음
				}
			}
		}
		System.out.println(memo[0][n][n] + memo[1][n][n] + memo[2][n][n]);
	}
}
