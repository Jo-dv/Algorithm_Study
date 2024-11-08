package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class BOJ_2295_세수의합 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static int[] u;
	static int answer = 0;

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		u = new int[n];
		for (int i = 0; i < n; i++)
			u[i] = Integer.parseInt(br.readLine());

		solve();
	}

	static void solve() {
		HashSet<Integer> check = new HashSet<>();
		for(int x: u)
			for(int y: u)
				check.add(x + y);

		for (int k = n - 1; k > -1; k--) {
			for (int z = k - 1; z > -1; z--) {
				if (check.contains(u[k] - u[z]))  // x + y = k - z
					answer = Math.max(answer, u[k]);
			}
		}
		
		System.out.println(answer);
	}
}