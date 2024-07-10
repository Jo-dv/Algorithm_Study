package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_7579_앱 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st, st1, st2;
	static int n, m;  // n개의 앱, 필요한 m의 메모리
	static int[] a;
	static int[] c;
	static int[] table;
	static int answer = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		a = new int[n];  // 메모리
		c = new int[n];  // 비용
		st1 = new StringTokenizer(br.readLine());
		st2 = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(st1.nextToken());
			c[i] = Integer.parseInt(st2.nextToken());
		}
		
		table = new int[(100 * n) + 1];  // 최대 100의 비용을 n개를 가질 수 있음
		
		solve();
			
	}
	
	static void solve() {
		for(int i = 0; i < n; i++)
			for(int j = (100 * n); j > c[i] - 1; j--) {
				table[j] = Math.max(table[j], table[j - c[i]] + a[i]);  // 특정 비용일 때 메모리의 최대
				if(m <= table[j])  // 임계값에 도달했을 때
					answer = Math.min(answer, j);  // 최소 비용 계산
			}
		
		System.out.println(answer);
	}
}
