package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_2533_사회망서비스 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int u, v;
	static ArrayList<Integer>[] tree;
	static int[][] dp;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		tree = new ArrayList[n + 1];
		dp = new int[n + 1][2];
		
		for(int i = 1; i <= n; i++) {
			tree[i] = new ArrayList<>();
		}
		
		for(int i = 0; i < n - 1; i++) {
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			tree[u].add(v);
			tree[v].add(u);
		}
		
		solve();
	}
	
	static void dfs(int current, boolean[] visited) {
		visited[current] = true;
		dp[current][0] = 0;
		dp[current][1] = 1;
		
		for(int next: tree[current]) {
			if(!visited[next]) {
				dfs(next, visited);
				dp[current][0] += dp[next][1];  // 자기 자신이 얼리어답터가 아니면 자식은 무조건 얼리어답터여야 함
				dp[current][1] += Math.min(dp[next][0], dp[next][1]);
			}
		}
		
	}
	
	static void solve() {
		boolean[] visited = new boolean[n + 1];
		dfs(1, visited);
		System.out.println(Math.min(dp[1][0], dp[1][1]));
	}

}
