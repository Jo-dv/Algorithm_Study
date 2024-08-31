package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10819_차이를최대로 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[] a;
	static boolean[] used;
	static int[] temp;
	static int answer;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		a = new int[n];
		temp = new int[n];
		used = new boolean[n];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++)
			a[i] = Integer.parseInt(st.nextToken());
		
		solve();
		System.out.println(answer);
	}
	
	static void search(int cnt) {  // 중복없는 재귀 O(n!), 합연산 O(n), O(n! * n)
		if(cnt == n) {
			int current_answer = 0;
			for(int i = 1; i < n; i++)
				current_answer += Math.abs(temp[i - 1] - temp[i]);
			answer = Math.max(answer, current_answer);
			return;
		}
		
		for(int i = 0; i < n; i++) {  // 중복없는 순열 계산
			if(used[i] == true)
				continue;
			temp[cnt] = a[i];
			used[i] = true;
			search(cnt + 1);
			temp[cnt] = 0;
			used[i] = false;
		}
	}
	
	static void solve() {
		search(0);
	}
}
