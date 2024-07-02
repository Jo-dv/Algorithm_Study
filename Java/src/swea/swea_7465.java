package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_7465 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int t, n, m;
	static int[] parents;
	static int answer;

	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			answer = 0;
			makeset();
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				union(from, to);
			}
			check();
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}

	static void makeset() {
		parents = new int[n + 1];
		for (int i = 1; i <= n; i++)
			parents[i] = i;
	}

	static int find(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find(parents[x]);
	}

	static void union(int x, int y) {
		x = find(x);
		y = find(y);
		if (x == y)
			return;
		parents[y] = x;
	}

	static void check() {
		for (int i = 1; i <= n; i++) {
			find(i);
			if (parents[i] == i)
				answer++;
		}
	}
}
