package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2169_로봇조종하기 {
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
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		solve();
	}
	
	static void solve() {
		int[][] dp = new int[n][m];
		for(int i = 0; i < n; i++)
			Arrays.fill(dp[i], -100);
		
		dp[0][0] = map[0][0];
		
		for(int i = 1; i < m; i++)
			dp[0][i] = dp[0][i - 1] + map[0][i];
		
		for(int i = 1; i < n; i++) {
			int[] left = new int[m];  // 각 행에 대한 열의 값을 저장할 배열
            int[] right = new int[m];
            
            left[0] = dp[i - 1][0] + map[i][0];  // 왼쪽 끝 아래로 내려와서
			for(int j = 1; j < m; j++) {  // 오른쪽 이동
				left[j] = map[i][j] + Math.max(left[j - 1], dp[i - 1][j]);
			}
			
			right[m - 1] = dp[i - 1][m - 1] + map[i][m - 1];  // 오른쪽 끝 아래로 내려와서
			for(int j = m - 2; j > -1; j--) {  // 왼쪽 이동
				right[j] = map[i][j] + Math.max(right[j + 1], dp[i - 1][j]);
			}
			
			for(int j = 0; j < m; j++)
				dp[i][j] = Math.max(left[j], right[j]);  //  왼쪽 이동과 오른쪽 이동 중 큰 값
		}
		
		System.out.println(dp[n - 1][m - 1]);
	}
}
