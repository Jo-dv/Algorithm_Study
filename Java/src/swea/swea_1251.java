package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class swea_1251 {
	static int t, n;
	static long answer;

	static int[] parent;
	static int[][] island; // 0: x, 1: y

	static long[][] edges;
	static double e;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			island = new int[n][2];

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++)
				island[i][0] = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++)
				island[i][1] = Integer.parseInt(st.nextToken());

			e = Double.parseDouble(br.readLine());

			parent = new int[n];
			makeset();

			int size = n * (n - 1) / 2; // n개의 정점을 연결하는 간선의 수
			edges = new long[size][3];

			int idx = 0;
			for (int v1 = 0; v1 < n - 1; v1++) {
				for (int v2 = v1 + 1; v2 < n; v2++) {
					edges[idx][0] = v1;
					edges[idx][1] = v2;
					edges[idx][2] = distance(island[v1][0], island[v2][0], island[v1][1], island[v2][1]);
					idx++;
				}
			}

			Arrays.sort(edges, (o1, o2) -> Long.compare(o1[2], o2[2]));
			answer = 0;
			int cnt = 0;

			for (int i = 0; i < size; i++) {
				// union 호출 대신 직접 코드 작성 - call stack save;
				int px = find((int) edges[i][0]);
				int py = find((int) edges[i][1]);

				if (px == py)
					continue;
				if (px > py)
					parent[py] = px;
				else
					parent[px] = py;

				answer += edges[i][2];
				cnt++;
				if (cnt == n - 1)
					break;
			}

			sb.append("#").append(tc).append(" ").append(Math.round(answer * e)).append("\n");
		}
		System.out.println(sb);

	}

	static long distance(int x1, int x2, int y1, int y2) {
		return (long) (Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
	}

	static void makeset() {
		for (int i = 0; i < n; i++)
			parent[i] = i;
	}

	static int find(int idx) {
		if (parent[idx] == idx)
			return idx;
		else
			return parent[idx] = find(parent[idx]);
	}

}
