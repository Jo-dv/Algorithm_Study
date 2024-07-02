package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1987 {
	static int r, c;
	static boolean[] visit = new boolean[26];
	static char[][] maps;
	static int answer = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		maps = new char[r][c];
		for(int i = 0; i < r; i++)
			maps[i] = br.readLine().toCharArray();
		dfs(0, 0, 0);
		System.out.println(answer);
	}
	
	static void dfs(int y, int x, int cnt) {
		answer = answer < cnt ? cnt : answer;
		if(y < 0 || y >= r || x < 0 || x >= c)
			return;
		if(!visit[(int)maps[y][x] - 65]) {
			visit[(int)maps[y][x] - 65] = true;
			dfs(y - 1, x, cnt + 1);
			dfs(y + 1, x, cnt + 1);
			dfs(y, x - 1, cnt + 1);
			dfs(y, x + 1, cnt + 1);
			visit[(int)maps[y][x] - 65] = false;
		}
	}
}
