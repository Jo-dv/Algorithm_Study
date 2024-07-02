package swea;

import java.util.Scanner;

public class swea_1954 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		int[][] direction = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

		for (int i = 1; i < t + 1; i++) {
			int n = in.nextInt();
			int[][] grid = new int[n][n];

			int y = 0;
			int x = -1;
			int num = 1;
			int my = 0;
			int mx = 0;

			while (num != Math.pow(n, 2) + 1) {
				for (int[] d : direction) {
					my = y + d[0];
					mx = x + d[1];
					while (0 <= my && my < n && 0 <= mx && mx < n) {
						if (grid[my][mx] == 0) {
							grid[my][mx] = num;
							num++;
							y = my;
							x = mx;
						}
						my += d[0];
						mx += d[1];
					}
				}
			}
			System.out.printf("#%d\n", i);
			for (int[] j : grid) {
				for (int k : j)
					System.out.print(k + " ");
				System.out.println();
			}
		}
	}
}
