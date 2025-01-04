package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_20926_얼음미로 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int w, h;
	static char[][] map;
	static int answer = 0;
	static Object tera;
	static Object exit;
	
	static class Object {
		int y, x, time;
		
		Object(int y, int x, int time) {
			this.y = y;
			this.x = x;
			this.time = time;
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		w = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		map = new char[h][w];
		
		for(int i = 0; i < h; i++) {
			String line = br.readLine();
			for(int j = 0; j < w; j++) {
				map[i][j] = line.charAt(j);
				if(map[i][j] == 'T') {
					tera = new Object(i, j, 0);
					map[i][j] = '0';
				}
				if(map[i][j] == 'E') {
					exit = new Object(i, j, 0);
				}
			}
		}
		
		solve();
	}
	
	static int slide(int y, int x, int dy, int dx) {
		int distance = 1;  // 한 칸 이동한 시점
		
		while(true) {
			int my = y + dy * distance;
			int mx = x + dx * distance;
			if(my < 0 || my >= h || mx < 0 || mx >= w || map[my][mx] == 'H') {  // 떨어지는 경우
				return -1;
			} else if(map[my][mx] == 'R') {  // 돌
				return distance - 1;
			} else if(map[my][mx] == 'E') {  // 출구
				return distance;
			}
			distance++;
		}
	}
	
	static void dijkstra() {
		int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		int[][] cost = new int[h][w];
		for(int i = 0; i < h; i++) {
			Arrays.fill(cost[i], Integer.MAX_VALUE);
		}
		cost[tera.y][tera.x] = 0;
		PriorityQueue<Object> pq = new PriorityQueue<>((o1, o2) -> o1.time - o2.time);
		pq.add(tera);
		
		while(!pq.isEmpty()) {
			Object current = pq.poll();
			
			for(int[] d: directions) {
				int distance = slide(current.y, current.x, d[0], d[1]);
				if(distance == -1) {  // 떨어진 경우 다음 방향 검사
					continue;
				}
				
				int my = current.y + d[0] * distance;
				int mx = current.x + d[1] * distance;
				int sliding_time = 0;
				for(int i = 1; i <= distance; i++) {
					if(map[current.y + d[0] * i][current.x + d[1] * i] != 'E') {  // 가장 끝 거리를 포함하는 시점에서 그곳이 도착점이라면 포함시키지 않는다.
						sliding_time += map[current.y + d[0] * i][current.x + d[1] * i] - '0';
					}
				}
				
				if(current.time + sliding_time < cost[my][mx]) {
					cost[my][mx] = current.time + sliding_time;
					pq.add(new Object(my, mx, cost[my][mx]));
				}
			}
		}
		System.out.println(cost[exit.y][exit.x] == Integer.MAX_VALUE ? -1 : cost[exit.y][exit.x]);
	}
	
	static void solve() {
		dijkstra();
	}
}
