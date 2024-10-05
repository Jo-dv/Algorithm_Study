package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1625_누울자리를찾아라 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static char[][] grid;
	static int[] answer = {0, 0};
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		grid = new char[n][n];
		
		for(int i = 0; i < n; i++) {
			String line = br.readLine();
			for(int j = 0; j < n; j++)
				grid[i][j] = line.charAt(j);
		}
		solve();
		
		System.out.println(answer[0] + " " + answer[1]);
	}
	
	static void solve() {
		for(int i = 0; i < n; i++) {
			int row = 0;
			int col = 0;
			
			for(int j = 0; j < n; j++)
				if(grid[i][j] == '.')
					row += 1;
				else {
					check(row, 0);
					row = 0;
				}
			for(int k = 0; k < n; k++)
				if(grid[k][i] == '.')
					col += 1;
				else {
					check(col, 1);
					col = 0;
				}
			check(row, 0);
			check(col, 1);
		}
	}
	
	static void check(int line, int idx) {
		if(line >= 2)
			answer[idx] += 1;
	}
}
