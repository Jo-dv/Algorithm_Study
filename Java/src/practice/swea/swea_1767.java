package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class swea_1767 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int t;
	static int n;
	static int[][] grid;
	static int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static List<Core> core_pos;
	static int max_core;
	static int answer;  // 최소 와이어 길이
	
	public static void main(String[] args) throws IOException{
		int t = Integer.parseInt(br.readLine());
		// core는 최대, 길이는 최소
		// 각 코어의 위치를 받아서 네 방향으로 완전 탐색, 가장 자리는 제외
		// dfs 사용
		for(int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			grid = new int[n][n];
			core_pos = new ArrayList<>();
			max_core = 0;
			answer = Integer.MAX_VALUE;
			
			for (int y = 0; y < n; y++) {  // 입력
				st = new StringTokenizer(br.readLine());
				for (int x = 0; x < n; x++) {
					grid[y][x] = Integer.parseInt(st.nextToken());
					if(grid[y][x] == 1 && (0 < y && y < n - 1 && 0 < x && x < n - 1))
						core_pos.add(new Core(y, x));
					else continue;
				}
			}
			
			// 실행 메서드
			dfs(0, 0, 0);
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
	
	static void dfs(int idx, int connected_core, int wire_len) {
		if(idx == core_pos.size()) {
			if(max_core < connected_core) {
				max_core = connected_core;
				answer = wire_len;
			}
			else if(max_core == connected_core)  // 현재 발견한 코어가 최대 코어와 동일하다면 둘 중 가장 짧은 전선을 사용한 경우를 채택
				answer = answer < wire_len ? answer : wire_len;
			return;
		}
		if(max_core > core_pos.size() - idx + connected_core)  
			// cell_pos.size() - idx: 현재 확인해야 할 코어의 수
			// 현재까지 연결한 코어의 수
			// 지금까지 갱신된 최대 코어보다 현재 코어 및 남은 코어의 합이 적다면 더 이상 해당 탐색을 진행할 필요가 없음
			return;
		
		int y = core_pos.get(idx).y;
		int x = core_pos.get(idx).x;
		int[][] origin = new int[n][n];
		for(int i = 0; i < n; i++) origin[i] = grid[i].clone();
		
		for (int[] d : direction) {
			int current_len = connect(y, x, d);
			if(current_len == 0)  // 연결을 못했다면 다음 코어 확인
				dfs(idx + 1, connected_core, wire_len);
			else
				dfs(idx + 1, connected_core + 1, wire_len + current_len);
			for(int i = 0; i < n; i++) grid[i] = origin[i].clone();
		}
	}
	
	static int connect(int y, int x, int[] d) {
		int result = 0;
		int my = y + d[0];
		int mx = x + d[1];
		
		while(0 <= my && my < n && 0 <= mx && mx < n) {
			if(grid[my][mx] == 1) return 0;  // 코어를 연결할 수 없는 경우
			grid[my][mx] = 1;
			result++;
			my += d[0];
			mx += d[1];
		}
		
		return result;
	}
	
	static class Core {
		int y, x;
		Core(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}

}
