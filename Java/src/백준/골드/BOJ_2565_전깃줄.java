package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2565_전깃줄 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static Node[] arr;
	
	static class Node {
		int s, e;

		public Node(int s, int e) {
			super();
			this.s = s;
			this.e = e;
		}
	}
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		arr = new Node[n];
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			arr[i] = new Node(s, e); 
		}
		
		solve();
	}

	static void solve() {
		int[] dp = new int[n];
		Arrays.fill(dp, 1);
		Arrays.sort(arr, (o1, o2) -> o1.s - o2.s);  // 시작점 기준으로 정렬해서 끝점들을 순차적으로 봤을 때 값이 오름차순이 아니라면 교차되는 구간
		
		for(int i = 1; i < n; i++) {
			for(int j = 0; j < i; j++) {
				if(arr[j].e < arr[i].e) {  // 교차되지 않는 전깃줄의 최장 길이 계산
					dp[i] = Math.max(dp[i], dp[j] + 1);
				}
			}
		}
		
		System.out.println(n - Arrays.stream(dp).max().getAsInt());
	}
}
