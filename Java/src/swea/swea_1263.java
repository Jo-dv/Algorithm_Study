package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_1263 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int T, N, min;
	static int INF = 999999;
	static int[][] graph;

	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			graph = new int[N][N];
			int n = 0;

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					n = Integer.parseInt(st.nextToken());
					if (i != j && n == 0)
						graph[i][j] = INF;
					else
						graph[i][j] = n;
				}
			}
			solve(tc);
		}
		System.out.println(sb);
	}

	static void solve(int tc) {
		for (int i = 0; i < N; i++) {
			for (int s = 0; s < N; s++) {
				if (s == i)
					continue;
				for (int e = 0; e < N; e++) {
					if (e == s || e == i)
						continue;
					graph[s][e] = Math.min(graph[s][e], graph[s][i] + graph[i][e]);
				}
			}
		}
		min = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			int sum = 0;
			for (int j = 0; j < N; j++)
				sum += graph[i][j];
			min = Math.min(min, sum);
		}
		sb.append("#").append(tc).append(" ").append(min).append("\n");
	}

}
