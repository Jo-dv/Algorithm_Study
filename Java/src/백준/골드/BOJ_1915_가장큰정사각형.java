package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1915_가장큰정사각형 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static char[][] arr;
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new char[n][m];
		
		for(int i = 0; i < n; i++) {
			String line = br.readLine();
			for(int j = 0; j < m; j++) {
				arr[i][j] = line.charAt(j);
			}
		}

		solve();
	}

	static void solve() {
		int[][] dp = new int[n + 1][m + 1];
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= m; j++) {
				if(arr[i - 1][j - 1] == '1') {
					dp[i][j] = 1;
				}
			}
		}
		
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= m; j++) {
				if(dp[i][j] == 1) {
					dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
					answer = Math.max(answer, dp[i][j]);
				}
			}
		}
		
		System.out.println(answer * answer);
	}
}
