package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_10971 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[][] cost;
	static boolean[] visit;
	static int answer;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		cost = new int[n][n];
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++)
				cost[i][j] = Integer.parseInt(st.nextToken());
		}
		answer = Integer.MAX_VALUE;
		
		for(int i = 0; i < n; i++) {
			visit = new boolean[n];
			visit[i] = true;
			dfs(i, i, 0);
		}
		
		System.out.println(answer);
	}
	
	static void dfs(int from, int to, int c) {
		if(check()) {
			if(cost[to][from] != 0)
                answer = Math.min(answer, c + cost[to][0]);
			return;
		}
		for(int i = 1; i < n; i++) {
			if(!visit[i] && cost[to][i] != 0) {
				visit[i] = true;
				dfs(from, i, c + cost[to][i]);
				visit[i] = false;
			}
		}
	}
	
	static boolean check() {
        for (int i = 0; i < n; i++)
            if (!visit[i]) 
                return false;
        return true;
    }
}
