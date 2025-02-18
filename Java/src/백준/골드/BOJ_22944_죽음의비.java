package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_22944_죽음의비 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, h, d;
	static char[][] grid;
	static int answer = Integer.MAX_VALUE;
	static ArrayList<Umbrella> umbrellas = new ArrayList<>(); 
	static boolean[] visited;
	static int ey, ex;
	
	static class Umbrella {
		int y, x;

		public Umbrella(int y, int x) {
			super();
			this.y = y;
			this.x = x;
		}
	}
	
	static class Player {
		int y, x, hp, durability, step;

		public Player(int y, int x, int hp, int durability, int cnt) {
			super();
			this.y = y;
			this.x = x;
			this.hp = hp;
			this.durability = durability;
			this.step = cnt;
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		grid = new char[n][n];
		for(int i = 0; i < n; i++) {
			String line = br.readLine();
			for(int j = 0; j < n; j++) {
				grid[i][j] = line.charAt(j);
				if(grid[i][j] == 'U') {
					umbrellas.add(new Umbrella(i, j));
				} if(grid[i][j] == 'E') {
					ey = i;
					ex = j;
				}
			}
		}
		visited = new boolean[umbrellas.size()];
		
		solve();
	}
	
	static void search(Player player) {
		if(player.hp + player.durability >= Math.abs(player.y - ey) + Math.abs(player.x - ex)) {
			answer = Math.min(answer, player.step + Math.abs(player.y - ey) + Math.abs(player.x - ex));
			return;
		}
		
		for(int i = 0; i < umbrellas.size(); i++) {
			int distance = Math.abs(player.y - umbrellas.get(i).y) + Math.abs(player.x - umbrellas.get(i).x);
			if(!visited[i] && player.hp + player.durability >= distance) {
				visited[i] = true;
				search(new Player(
						umbrellas.get(i).y, 
						umbrellas.get(i).x, 
						player.durability < distance ? player.hp - (distance - player.durability) : player.hp,
								d, 
								player.step + distance)
						);
				visited[i] = false;
			}
		}
	}

	static void solve() {
		Player player = null;
		
		loop:
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(grid[i][j] == 'S') {
					grid[i][j] = '.';
					player = new Player(i, j, h, 0, 0);
					break loop;
				}
			}
		}
		
		search(player);
		
		System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
	}
}