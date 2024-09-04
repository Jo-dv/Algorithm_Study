package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_15486_퇴사2 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[][] arr;
	static int answer = 0;

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		arr = new int[n + 1][2];
		
		for(int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			int t = Integer.parseInt(st.nextToken());
			int p = Integer.parseInt(st.nextToken());
			arr[i][0] = t;
			arr[i][1] = p;
		}
		
		solve();
	}
	
	static void solve() {
		int[] dp = new int[n + 1];
		
		for(int i = 1; i <= n; i++) {
            dp[i] = Math.max(dp[i], dp[i - 1]);  // 오늘날까지의 최대 수익
			
			int end = (i - 1) + arr[i][0];  // 현재 날부터(i) 해당하는 근무를(arr[i][0]) 마쳤을 때의 날 
            if (end <= n)  // 근무가 퇴사하는 날 안에 끝난다면
                dp[end] = Math.max(dp[end], dp[i - 1] + arr[i][1]);  // 기존 해당 일에 끝났을 때 비용과 해당 업무가 끝났을 때 비용을 비교
            // end나 dp 값 갱신에서 i가 아닌 i-1을 사용하는 이유는 근무가 i도 포함되기 때문, 즉 2일에 시작해서 5일을 일하면 7일에 끝이아닌 6일에 끝이남
            // arr[i]인 이유는 데이터 자체는 올바르게 i 그대로 가리키고 있기 때문
		}

		System.out.println(dp[n]);
	}
}