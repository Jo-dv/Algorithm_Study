package 백준.실버;

import java.io.*;
import java.util.*;

public class BOJ_11055_가장큰증가하는부분수열 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[] a;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		a = new int[n];
		st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i < n; i++)
			a[i] = Integer.parseInt(st.nextToken());
		
		solve();
	}
	
	static void solve() {
		int[] dp = new int[n];
		for(int i = 0; i < n; i++)  // 초기값으로 자기 자신을 가짐 -> 비교하지 않았기 때문에 자기 자신이 그 위치에서 가장 큰 값
			dp[i] = a[i];
		
		for(int i = 1; i < n; i++)
			for(int j = 0; j < i; j++)
				if(a[j] < a[i])
					dp[i] = Math.max(dp[i], dp[j] + a[i]);
		
		System.out.println(Arrays.stream(dp).max().getAsInt());
	}
}
