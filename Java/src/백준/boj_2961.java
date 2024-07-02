package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2961 {
	static int n;
	static int[][] ingredient;
	static boolean[] check;
	static int s = 1;
	static int b = 0;
	static int answer = Integer.MAX_VALUE;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		ingredient = new int[n][2];
		StringTokenizer st;
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			ingredient[i][0] = Integer.parseInt(st.nextToken());
			ingredient[i][1] = Integer.parseInt(st.nextToken());
		}
		check = new boolean[n];
		search(0);
		System.out.println(answer);
	}
	
	static void search(int idx) {
		s = 1;
		b = 0;
		if(idx == n) {
			for (int i = 0; i < n; i++) {
				if(check[i]) {
					s *= ingredient[i][0];
					b += ingredient[i][1];
				}
			}
			if (s != 1 || b != 0)
				answer = (Math.abs(s - b) < answer) ? Math.abs(s - b) : answer;
			return;
		}
		check[idx] = true;
		search(idx + 1);
		check[idx] = false;
		search(idx + 1);
	}
}