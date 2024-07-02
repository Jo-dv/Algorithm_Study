package 백준;

import java.util.Scanner;

public class boj_15650 {
	static int[] problem;
	static int[] result;
	static int n;
	static int m;
	static StringBuilder sb;

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		sb = new StringBuilder();
		n = in.nextInt();
		m = in.nextInt();
		problem = new int[n];
		for (int i = 1; i < n + 1; i++)
			problem[i - 1] = i;
		result = new int[m];
		solve(0, 0);
		System.out.println(sb);

	}

	static void solve(int idx, int target) {
		if (target == m) {
			for (int i : result)
				sb.append(i).append(" ");
			sb.append("\n");
			return;
		}
		if (idx == n)
			return;
		result[target] = problem[idx];
		solve(idx + 1, target + 1);
		solve(idx + 1, target);
	}

}
