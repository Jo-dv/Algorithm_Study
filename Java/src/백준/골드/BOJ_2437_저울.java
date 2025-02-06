package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2437_저울 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[] balance;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		balance = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			balance[i] = Integer.parseInt(st.nextToken());
		}
		
		solve();
	}
	
	static void solve() {
		Arrays.sort(balance);
		int result = 1;  // 최소가 1
		
		for(int weight: balance) {
			if(result < weight) {
				break;
			}
			result += weight;
		}
		
		System.out.println(result);
	}
}
