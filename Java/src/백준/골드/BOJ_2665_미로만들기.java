package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;

public class BOJ_2665_미로만들기 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static char[][] map;

	static class Node {
		int y, x, cnt;

		public Node(int y, int x, int cnt) {
			this.y = y;
			this.x = x;
			this.cnt = cnt;
		}
	}

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		map = new char[n][n];

		for (int i = 0; i < n; i++) {
			String line = br.readLine();
			for (int j = 0; j < n; j++) {
				map[i][j] = line.charAt(j);
			}
		}

		solve();
	}

	static void solve() {
		ArrayDeque<Node> dq = new ArrayDeque<>();
		int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
		int[][] costs = new int[n][n];
		for (int[] i : costs) {
			Arrays.fill(i, n * n + 1);
		}
		costs[0][0] = 0;
		dq.add(new Node(0, 0, 0));

		while (!dq.isEmpty()) {
			Node current = dq.pollFirst();
			if (current.y == n - 1 && current.x == n - 1) {
				System.out.println(costs[n - 1][n - 1]);
				return;
			}

			if (costs[current.y][current.x] < current.cnt) {  // 현재 서있는 곳이 이미 최소로 갱신 돼 있다면
				continue;
			}

			for (int[] d : directions) {
				int my = current.y + d[0];
				int mx = current.x + d[1];

				if (0 <= my && my < n && 0 <= mx && mx < n) {
					int new_cost = map[my][mx] == '1' ? current.cnt : current.cnt + 1;
					if (new_cost < costs[my][mx]) {
						costs[my][mx] = new_cost;
						if (current.cnt == new_cost) {
							dq.addFirst(new Node(my, mx, current.cnt));
						} else {
							dq.addLast(new Node(my, mx, current.cnt + 1));
						}
					}
				}
			}
		}
	}
}
