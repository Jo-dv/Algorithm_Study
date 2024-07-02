package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class swea_5643 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int t;
	static int n, m;
	static int a, b;
	static int[] check;
	static List<List<Integer>> graph = new ArrayList<>();
	static List<List<Integer>> reverse_graph = new ArrayList<>();
	static int answer;

	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			m = Integer.parseInt(br.readLine());
			check = new int[n + 1];
			answer = 0;
			graph = new ArrayList<>();
			reverse_graph = new ArrayList<>();
			graph.add(new ArrayList<>());
			reverse_graph.add(new ArrayList<>());
			for (int i = 0; i < n; i++) {
				graph.add(new ArrayList<>());
				reverse_graph.add(new ArrayList<>());
			}
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				graph.get(a).add(b);
				reverse_graph.get(b).add(a);
			}
			solve(graph);
			solve(reverse_graph);
			for (int i : check)
				answer += (i == n - 1 ? 1 : 0);
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
//			System.out.println(Arrays.toString(check));
//			for (List<Integer> i : graph) {
//				System.out.println(i.toString());
//			}
		}
		System.out.println(sb);
	}

	static void solve(List<List<Integer>> g) {
		Queue<Integer> q;
		for (int i = 1; i <= n; i++) {
			int cnt = 0;
			boolean[] visited = new boolean[n + 1];
			q = new ArrayDeque<Integer>();
			q.offer(i);
			visited[i] = true;

			while (!q.isEmpty()) {
				int node = q.poll();
				for (int j : g.get(node)) {
					if (!visited[j]) {
						visited[j] = true;
						q.offer(j);
						cnt += 1;
					}
				}
			}
			check[i] += cnt;
		}
	}

}
