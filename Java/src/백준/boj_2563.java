package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2563 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		int[][] range = new int[n][2];
		boolean[][] paper = new boolean[101][101];
		int answer = 0;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			range[i][0] = Integer.parseInt(st.nextToken());
			range[i][1] = Integer.parseInt(st.nextToken());
		}

		for (int[] r : range)
			for (int y = r[1]; y < r[1] + 10; y++)
				for (int x = r[0]; x < r[0] + 10; x++) {
					if (!paper[y][x]) {
						paper[y][x] = true;
						answer++;
					}
				}
		System.out.println(answer);
	}
}
