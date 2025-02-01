package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_13422_도둑 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int t;
	static int n, m, k;
	static int[] money;
	static int answer;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		
		for(int tc = 0; tc < t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			
			money = new int[n];
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i < n; i++) {
				money[i] = Integer.parseInt(st.nextToken());
			}
			answer = 0;
			
			solve();
		}
		
		System.out.println(sb);
	}
	
	static void solve() {
		int temp = 0;
		int low = 0;
		int high = m - 1;
		for(int i = 0; i < m; i++) {
			temp += money[i];
		}
		if(temp < k) {
			answer++;
		}
		
		if(n != m) {
			while(low < n - 1) {
				temp -= money[low++];
				temp += money[(++high) % n];
				if(temp < k) {
					answer++;
				}
			}
		}
		
		sb.append(answer).append("\n");
	}
}
