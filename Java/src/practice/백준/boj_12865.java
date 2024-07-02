package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_12865 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, k;
	static int[] weight, value;
	static int[][] dp;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		weight = new int[n + 1];
		value = new int[n + 1];
		dp = new int[n + 1][k + 1];
		
		for(int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			weight[i] = Integer.parseInt(st.nextToken());
			value[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i = 1; i <= n; i++) {
			int w = weight[i];
			int v = value[i];
			
			for(int ki = 1; ki <= k; ki++) {
				if(w <= ki)
					dp[i][ki] = Math.max(dp[i - 1][ki], dp[i - 1][ki - w] + v);  // 선택 및 비선택
				else
					dp[i][ki] = dp[i - 1][ki];
			}
		}
		System.out.println(dp[n][k]);

	}

}
