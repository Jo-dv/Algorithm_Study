package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class swea_2001 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc < t + 1; tc++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			int[][] arr = new int[n][n];

			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int best = -1;
			int size = n - m + 1;
			for(int stride = 0; stride < size; stride++)
				for(int col = 0; col < size; col++) {
					int kill = 0;
					for(int row = 0; row < m; row++)
						kill += Arrays.stream(Arrays.copyOfRange(arr[row+stride], col, col + m)).sum();
					best = (kill > best) ? kill : best;
				}
			System.out.printf("#%d %d", tc, best);
		}
	}
}
