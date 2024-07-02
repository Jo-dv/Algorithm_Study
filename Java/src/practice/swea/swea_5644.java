package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_5644 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		StringTokenizer st;
		int[][] direction = {{0, 0}, {0, -1}, {-1, 0}, {0, 1}, {1, 0}};
		
		int T = Integer.parseInt(br.readLine());
		for(int t = 1; t <= T; t++) {
			int sum_A = 0, sum_B = 0;
			st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());
			int A = Integer.parseInt(st.nextToken());
			int[] player_A = new int[M + 1], player_B = new int[M + 1];
			int[][] bc = new int[A][];
			st = new StringTokenizer(br.readLine());
			for(int i = 1; i <= M; i++)
				player_A[i] = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			for(int i = 1; i <= M; i++)
				player_B[i] = Integer.parseInt(st.nextToken());
			for(int i = 0; i < A; i++) {
				st = new StringTokenizer(br.readLine());
				int ap_x = Integer.parseInt(st.nextToken());
				int ap_y = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				int p = Integer.parseInt(st.nextToken());
				bc[i] = new int[] {ap_x, ap_y, c, p};
			}
		}
	}

}
