package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_19236_청소년상어 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] info = new int[4][8];
	static int[][] grid = new int[4][4];
	static Fish[] fishes = new Fish[17];
	static int[][] directions = {{-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
	static int answer = 0;
	
	static class Pos {
		int y, x, d;

		public Pos(int y, int x, int d) {
			this.y = y;
			this.x = x;
			this.d = d;
		}

		@Override
		public String toString() {
			return "Pos [y=" + y + ", x=" + x + ", direction=" + d + "]";
		}
	}
	
	static class Fish extends Pos {
		boolean dead;

		public Fish(int y, int x, int direction, boolean dead) {
			super(y, x, direction);
			this.dead = dead;
		}

		@Override
		public String toString() {
			return "Fish [y=" + y + ", x=" + x + ", dead=" + dead + "]";
		}
	}

	public static void main(String[] args) throws IOException {
		for(int i = 0; i < 4; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < 4; j++) {
				int num = Integer.parseInt(st.nextToken());
				int dir = Integer.parseInt(st.nextToken()) - 1;
				grid[i][j] = num;
				fishes[num] = new Fish(i, j, dir, false);
			}
		}
		
		solve();
	}
	
	static void move_fish(int[][] new_grid, Fish[] new_fishes, Pos shark) {
		for(int i = 1; i <= 16; i++) {
			Fish fish = new_fishes[i];
			if(fish.dead) {
				continue;
			}
			
			for(int j = 0; j < 8; j++) {
				int md = (fish.d + j) % 8;
				int my = fish.y + directions[md][0];
				int mx = fish.x + directions[md][1];
				
				if(0 <= my && my < 4 && 0 <= mx && mx < 4 && !(my == shark.y && mx == shark.x)) {
					if(new_grid[my][mx] == 0) {
						new_grid[my][mx] = new_grid[fish.y][fish.x];
						new_grid[fish.y][fish.x] = 0;
					} else {
						int existing_fish = new_grid[my][mx];
						new_grid[my][mx] = new_grid[fish.y][fish.x];
						new_grid[fish.y][fish.x] = existing_fish;
						new_fishes[existing_fish].y = fish.y;
						new_fishes[existing_fish].x = fish.x;
					}
					fish.y = my;
					fish.x = mx;
					fish.d = md;
					
					break;
				}
			}
		}
	}
	
	static void move_shark(int y, int x, Pos shark, int score, int[][] grid, Fish[] fishes) {
		answer = Math.max(answer, score);
		
		int[][] new_grid = new int[4][4];
		Fish[] new_fishes = new Fish[17];
		for(int i = 0; i < 4; i++) {
			new_grid[i] = grid[i].clone();
		}
		
		for(int i = 1; i <= 16; i++) {
			new_fishes[i] = new Fish(fishes[i].y, fishes[i].x, fishes[i].d, fishes[i].dead);
		}
		
		move_fish(new_grid, new_fishes, shark);
		
		for(int i = 1; i <= 3; i++) {
			int my = shark.y + directions[shark.d][0] * i;
			int mx = shark.x + directions[shark.d][1] * i;
			
			if(0 <= my && my < 4 && 0 <= mx && mx < 4 && new_grid[my][mx] != 0) {
				int fish = new_grid[my][mx];
				int md = new_fishes[fish].d;
				new_grid[my][mx] = 0;
				new_fishes[fish].dead = true;
				move_shark(my, mx, new Pos(my, mx, md), score + fish, new_grid, new_fishes);
				new_grid[my][mx] = fish;
				new_fishes[fish].dead = false;
			}			
		}
		
	}

	static void solve() {
		Pos shark = new Pos(-1, -1, -1);
		int fish = grid[0][0];
		shark.y = 0;
		shark.x = 0;
		shark.d = fishes[fish].d;
		fishes[fish].dead = true;
		grid[0][0] = 0;
		
		move_shark(0, 0, shark, fish, grid, fishes);
		
		System.out.println(answer);
	}

}
