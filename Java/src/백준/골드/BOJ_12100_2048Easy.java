package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_12100_2048Easy {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[][] grid;
	static int[] directions = {1, 2, 3, 4};  // 상좌하우
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		grid = new int[n][n];
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++)
				grid[i][j] = Integer.parseInt(st.nextToken());
		}
		
		solve();
	}
	
	static void move(int dir) {
		boolean[][] visited = new boolean[n][n];
		
		if(dir == 1) {
			for(int x = 0; x < n; x++)
				for(int y = 1; y < n; y++) {
					int current = y;
					while(current >= 1 && grid[current - 1][x] == 0) {  // 이동시킬 숫자가 있고 다음 이동 방향이 빈 칸일 때
						grid[current - 1][x] += grid[current][x];
						grid[current][x] = 0;
						current--;
					}
					if(current >= 1 && grid[current][x] == grid[current - 1][x] && !visited[current - 1][x]) {  // 이동이 끝나고 다음 이동 방향의 숫자가 동일하고 아직 합쳐지지 않은 숫자라면
						// current를 검사하는 이유는, 단순히 0이 됐을 때 인덱싱 에러가 발생하므로
						grid[current - 1][x] *= 2; // 하나로 합침
						grid[current][x] = 0;
						visited[current - 1][x] = true;
					}
				}
		}
		else if(dir == 2)
			for(int y = 0; y < n; y++)
				for(int x = 1; x < n; x++) {
					int current = x;
					while(current >= 1 && grid[y][current - 1] == 0) {
						grid[y][current - 1] += grid[y][current];
						grid[y][current] = 0;
						current--;
					}
					if(current >= 1 && grid[y][current] == grid[y][current - 1] && !visited[y][current - 1]) {
						grid[y][current - 1] *= 2;
						grid[y][current] = 0;
						visited[y][current - 1] = true;
					}
				}
		else if(dir == 3)
			for(int x = 0; x < n; x++)
				for(int y = n - 2; y > - 1; y--) {
					int current = y;
					while(current <= n - 2 && grid[current + 1][x] == 0) {
						grid[current + 1][x] += grid[current][x];
						grid[current][x] = 0;
						current++;
					}
					if(current <= n - 2 && grid[current][x] == grid[current + 1][x] && !visited[current + 1][x]) {
						grid[current + 1][x] *= 2;
						grid[current][x] = 0;
						visited[current + 1][x] = true;
					}
				}
		else
			for(int y = 0; y < n; y++)
				for(int x = n - 2; x > - 1; x--) {
					int current = x;
					while(current <= n - 2 && grid[y][current + 1] == 0) {
						grid[y][current + 1] += grid[y][current];
						grid[y][current] = 0;
						current++;
					}
					if(current <= n - 2 && grid[y][current] == grid[y][current + 1] && !visited[y][current + 1]) {
						grid[y][current + 1] *= 2;
						grid[y][current] = 0;
						visited[y][current + 1] = true;
					}
				}
	}
	
	static void check() {
		for(int y = 0; y < n; y++)
			for(int x = 0; x < n; x++)
				answer = Math.max(answer, grid[y][x]);
	}
	
	static void search(int cnt) {
		check();
		if(cnt == 5)  // 5번까지 움직였으면 종료
			return;
		
		int[][] backup = new int[n][n];
        for (int i = 0; i < n; i++)
            backup[i] = grid[i].clone(); // grid 상태 저장

		for(int d = 1; d <= 4; d++) {
			move(d);
			search(cnt + 1);
			
			for (int i = 0; i < n; i++)
                grid[i] = backup[i].clone(); // 상태 복구
		}		
	}
	
	static void solve() {
		search(0);
		System.out.println(answer);
	}
}
