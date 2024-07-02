package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class swea_3124_2 {
	static int[][] nodes;
	static int[] parent;
	static long answer;
	static int cnt = 0;
	static List<List<int[][]>> adjList;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			st = new StringTokenizer(br.readLine());
			int v = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			nodes = new int[e + 1][3];
			parent = new int[v + 1];
			answer = 0;
			Arrays.sort(nodes, (o1, o2) -> o1[2] - o2[2]);

			for (int i = 1; i <= e; i++) {
				st = new StringTokenizer(br.readLine());
				nodes[i][0] = Integer.parseInt(st.nextToken());
				nodes[i][1] = Integer.parseInt(st.nextToken());
				nodes[i][2] = Integer.parseInt(st.nextToken());
			}

			for (int i = 1; i <= v; i++)
				parent[i] = i;

			for (int i = 1; i <= v; i++) {
				if (find(nodes[i][0]) != find(nodes[i][1])) {
					union(nodes[i][0], nodes[i][1]);
					answer += nodes[i][2];
					cnt++;
				}
				if (cnt == v - 1)
					break;
			}

			sb.append("#").append(tc).append(" ").append(answer);
		}

		System.out.println(sb);
	}

	static int find(int x) {
		if (parent[x] == x)
			return x;
		else
			return parent[x] = find(parent[x]);
	}

	static void union(int x, int y) {
		int px = find(x);
		int py = find(y);
		parent[px] = py;
	}

}