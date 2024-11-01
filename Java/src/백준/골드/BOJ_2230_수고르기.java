package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2230_수고르기 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static int[] a;
	static int answer = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		a = new int[n];
		for(int i = 0; i < n; i++)
			a[i] = Integer.parseInt(br.readLine());
		
		solve();
	}
	
	static void solve() {
		Arrays.sort(a);
		int low = 0, high = 0;
		int temp = 0;
		
		while(low <= high && high < n) {
			temp = a[high] - a[low];
			if(temp >= m)
				answer = Math.min(answer, temp);
			if(temp < m)
				high++;
			else
				low++;
		}
		System.out.println(answer);
	}
}
