package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class swea_1861_다시풀어보기 {  // 못풀었음

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		
		int tc = Integer.parseInt(br.readLine());
		for(int t = 1; t < tc + 1; t++) {
			Deque<int []> q = new ArrayDeque<int []>();
			int n = Integer.parseInt(br.readLine());
			int[][] grid = new int[n][n];
			int[] position = {0, 1};
			int[] answer = {-1, -1};
			
			for(int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j < n; j++)
					grid[i][j] = Integer.parseInt(st.nextToken());
			}
			
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					q.add(new int[] {i, j});
					
					while(!q.isEmpty()) {
						int[] yx = q.pollFirst();
						int y = yx[0];
						int x = yx[1];
						
						for (int[] d : direction) {
							int my = y + d[0];
							int mx = x + d[1];
							
							if(0 <= my && my < n && 0 <= mx && mx < n) {
								if(grid[y][x] == grid[my][mx] - 1) {
									if(position[0] == 0)
										position[0] = grid[y][x];
									position[1]++;
								}
							}
						}
					}
				}
			}
			System.out.printf("#%d %d %d\n", t, answer[0], answer[1]);
		}

	}

}
