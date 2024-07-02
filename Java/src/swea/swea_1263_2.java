package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class swea_1263_2 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int T, N, min;
	static ArrayList<ArrayList<Integer>> adj;
	static int INF = 999999;

	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			adj = new ArrayList<>();
			for (int i = 0; i < N; i++)
				adj.add(new ArrayList<>());

			int n = 0;

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					n = Integer.parseInt(st.nextToken());
					if (n == 1)
						adj.get(i).add(j);
				}
			}
			solve(tc);
		}
		System.out.println(sb);
	}

	static void solve(int tc) {
		// 각 정점 별로 각자 최단 경로 탐색 후 min 갱신
		min = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			bfs(i);
		}
		sb.append("#").append(tc).append(" ").append(min).append("\n");
	}

	static void bfs(int V) {
		Queue<Node> q = new ArrayDeque<>();
		boolean[] visit = new boolean[N];

		visit[V] = true;
		q.offer(new Node(V, 0));

		int dist = 0;
		while (!q.isEmpty()) {
			Node node = q.poll();
			// node.v -> adj.get(node.v)
			for (int v : adj.get(node.v)) {
				if (visit[v])
					continue;
				dist += node.cnt + 1;
				if (dist >= min)
					return; // 가지치기

				visit[v] = true;
				q.offer(new Node(v, node.cnt + 1));

			}
		}

		min = Math.min(min, dist);

	}

	static class Node {
		int v, cnt;

		public Node(int v, int cnt) {
			this.v = v;
			this.cnt = cnt;
		}
	}

}
