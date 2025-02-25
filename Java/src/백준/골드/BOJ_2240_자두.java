package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2240_자두 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int t, w;
	static int[] plum;
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		t = Integer.parseInt(st.nextToken());
		w = Integer.parseInt(st.nextToken());
		plum = new int[t + 1];
		for(int i = 1; i <= t; i++) {
			plum[i] = Integer.parseInt(br.readLine());
		}
		
		solve();
	}

	static void solve() {
		int[][][] dp = new int[t + 1][w + 1][3];
		
		if(plum[1] == 1) {  // 시작부터 1번 나무에서 떨어지는 경우
			dp[1][0][1] = 1;
		} else {
			dp[1][1][2] = 1;
		}
		
		for(int i = 2; i <= t; i++) {  // 두 번째부터
			if(plum[i] == 1) {  // 1번 나무에서 떨어지는 경우
				dp[i][0][1] = dp[i - 1][0][1] + 1;  // 1번 나무에 있을 경우
				dp[i][0][2] = dp[i - 1][0][2];  // 2번 나무에 있을 경우(이전 시점에서 이동) -> 먹지 못함
				
				for(int j = 1; j <= w; j++) {  // 움직이기 시작함
					dp[i][j][1] = Math.max(dp[i - 1][j][1], dp[i - 1][j - 1][2]) + 1;  // 1번 나무에 그대로 있었거나(사실상 이전 시점에서 안 움직인 경우) 2번 나무에서 1번으로 이동한 경우
					dp[i][j][2] = Math.max(dp[i - 1][j - 1][1], dp[i - 1][j][2]);  // 1번 나무에서 2번 나무로 이동했거나, 이전 시점에서 2번 나무로 이동했기에 어떤 경우도 먹지 못함
				}
			} else {  // 첫 케이스와는 완전히 반대
				dp[i][0][1] = dp[i - 1][0][1];  // 1번 나무에 있어서 먹지 못함
				dp[i][0][2] = dp[i - 1][0][2] + 1;  // 2번 나무라서 먹음
				
				for(int j = 1; j <= w; j++) {
					dp[i][j][1] = Math.max(dp[i - 1][j][1], dp[i - 1][j - 1][2]);  // 1번에 그대로 있거나 2번에서 1번으로 이동한 경우
					dp[i][j][2] = Math.max(dp[i - 1][j - 1][1], dp[i - 1][j][2]) + 1;  // 1번에서 2번으로 이동했거나 2번에 그대로 있는 경우
				}
			}
		}
		
		for(int i = 0; i <= w; i++) {
			answer = Math.max(answer, Math.max(dp[t][i][1], dp[t][i][2]));
		}
		
		System.out.println(answer);
	}
}
