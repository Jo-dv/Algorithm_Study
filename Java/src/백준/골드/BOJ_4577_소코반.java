package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_4577_소코반 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int r, c;
	static char[][] grid;
	static String command;
	static StringBuilder sb = new StringBuilder();
	static Map<Character, int[]> directions = Map.of(
			'U', new int[] {-1, 0}, 
			'D', new int[] {1, 0}, 
			'L', new int[] {0, -1}, 
			'R', new int[] {0, 1});
	
	public static void main(String[] args) throws IOException {
		int t = 0;
		while(true) {
			st = new StringTokenizer(br.readLine());
			r = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			if(r == 0 && c == 0)
				break;
			
			grid = new char[r][c];
			
			for(int i = 0; i < r; i++) {
				String line = br.readLine();
				for(int j = 0; j < c; j++) {
					grid[i][j] = line.charAt(j);
				}
			}
			
			command = br.readLine();
			
			sb.append("Game ").append(++t).append(": ").append(solve() ? "complete" : "incomplete").append("\n");
			for(char[] i: grid) {
				for(char j: i)
					sb.append(j);
				sb.append("\n");
			}
		}
		System.out.println(sb);
	}
	
	static Player search_chracter() {
		int y = 0, x = 0;
		loop: for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
				if(grid[i][j] == 'w' || grid[i][j] == 'W') {
					y = i;
					x = j;
					break loop;
				}
		
		char current = grid[y][x] == 'w' ? '.' : '+';
		return new Player(grid[y][x], current, y, x);
	}
	
	static int count_target() {
		int target = 0;
		
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
				if(grid[i][j] == '+' || grid[i][j] == 'W')  // 모든 목표점에 대해
					target++;
		
		return target;
	}

	static boolean move(Player player) {
		int len = command.length();
		int target = count_target();
		
		for(int i = 0; i < len; i++) {
			char c = command.charAt(i);
			int[] d = directions.get(c);
			
			int my = player.y + d[0];
			int mx = player.x + d[1];
			if(0 <= my && my < r && 0 <= mx && mx < c) {  // 유효 범위라면
				if(grid[my][mx] == '#')  // 벽이면 이동 불가
					continue;
				
				if(grid[my][mx] == '.') {
					grid[player.y][player.x] = player.current;  // 플레이어가 있던 자리 원상 복귀
					player.y = my;
					player.x = mx;
					
					player.current = '.';  // 이동한 곳의 공간
					player.state = 'w';
					grid[my][mx] = player.state;  // 플레이어 이동
				}
				else if(grid[my][mx] == '+') {
					grid[player.y][player.x] = player.current;  // 플레이어가 있던 자리 원상 복귀
					player.y = my;
					player.x = mx;
					
					player.current = '+';
					player.state = 'W';
					grid[my][mx] = player.state;
				}
				else {  // 벽돌인 경우
					int next_y = my + d[0];  // 벽돌을 옮길 위치
					int next_x = mx + d[1];
					
					if(0 <= next_y && next_y < r && 0 <= next_x && next_x < c) {
						if(grid[next_y][next_x] == '#' || grid[next_y][next_x] == 'b' || grid[next_y][next_x] == 'B')
							continue;
						
						if(grid[next_y][next_x] == '+') {  // 박스가 이동할 곳이 목표점이라면
							grid[next_y][next_x] = 'B';
							target--;  // 박스를 목표점에 옮겼으므로 하나 제거
						}
						else
							grid[next_y][next_x] = 'b';
						
						if(grid[my][mx] == 'B') {  // 목표점에 있는 박스를 옮겼으니 해당 자리는 목표점으로 원상 복귀
							grid[my][mx] = '+';
							target++;  // 목표점에 있던 상자가 위치를 벗어났으므로 하나 추가
						}
						else
							grid[my][mx] = '.';  // 목표점이 아니라면 빈 공간 밖에 없음
						
						grid[player.y][player.x] = player.current;  // 플레이어를 옮길 것이므로 현재 밟고 있는 공간 초기화
						player.y = my;
						player.x = mx;
						
						player.current = grid[my][mx];  // player 이동
						player.state = player.current == '+' ? 'W' : 'w';  // 이동한 공간에 따라 형태 변경
						grid[my][mx] = player.state;  // 상태 변경 반영
						
						if(target == 0)  // 현재 움직이 끝났을 때, 모든 박스를 옮겼다면 게임 즉시 종료
							return true;
					}
				}
			}
		}
		
		return false;
	}
	
	static boolean solve() {
		Player player = search_chracter();  // 플레이어 위치 탐색
		return move(player);  // 플레이어 이동
	}
	
	static class Player {
		char state, current;
		int y, x;
		
		Player(char state, char current, int y, int x) {
			this.state = state;  // 현재 상태
			this.current = current;  // 현재 위치한 공간
			this.y = y;
			this.x = x;
		}
	}
}
