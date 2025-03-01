package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_13398_연속합2 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[] arr;
	static int answer;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		solve();
	}

	static void solve() {
		int[][] dp = new int[n][2];
		dp[0][1] = arr[0];  // 값 제거하지 않았을 때
		answer = arr[0];
		
		for(int i = 1; i < n; i++) {
			dp[i][0] = Math.max(dp[i - 1][1], dp[i - 1][0] + arr[i]);  // 현재 값 삭제 or 이전에 한 번 삭제 됐으니 누적
			dp[i][1] = Math.max(dp[i - 1][1] + arr[i], arr[i]);  // 누적 or 현재값부터
			answer = Math.max(answer, Math.max(dp[i][0], dp[i][1]));
		}
		
		System.out.println(answer);
	}
}
