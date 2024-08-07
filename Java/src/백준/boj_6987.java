package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_6987 {
	static int[] win, lose, draw;  // 승, 패, 무 결과를 저장
	static int[][] game; // for - for match 진행을 이어갈 배열
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		win = new int[6];
		lose = new int[6];
		draw = new int[6];
		
		// game 배열 2팀이 각각 1:1 시합을 이어나가는 형태, 15 게임
		// 0 0 0 0 0 1 1 1 1 2 2 2 3 3 4
		// 1 2 3 4 5 2 3 4 5 3 4 5 4 5 5
		game = new int[15][2];
		int idx = 0;
		
		for (int i = 0; i < 5; i++) {
			for (int j = i + 1; j < 6; j++) {
				game[idx][0] = i;
				game[idx][1] = j;
				idx++;
			}
		}
		
		// 입력
		for (int i = 0; i < 4; i++) {
			int sum = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 6; j++) {  // 3개씩 끊어서
				sum += win[j] = Integer.parseInt(st.nextToken());
				sum += draw[j] = Integer.parseInt(st.nextToken());
				sum += lose[j] = Integer.parseInt(st.nextToken());
			}
			if(sum != 30) {  // 유효하지 않음
				System.out.print("0 ");
				continue;
			}
			
			// 완탐
			if(dfs(0))
				System.out.print("1 ");
			else
				System.out.print("0 ");
		}
	}
	
	// game 배열을 이용해서 모든 1:1 게임을 순차적으로 진행하면서 win, lose, draw 자료구조의 유효성 검증
	// 가지치기 - win, lose, draw에 대해서 각 배열이 양수일 때만 진행
	// game 배열의 마지막까지 도달하면 유효한 결과
	static boolean dfs(int idx) {
		if(idx == 15)
			return true;
		int teamA = game[idx][0];
		int teamB = game[idx][1];
		
		// a팀이 이기는 경우
		if(win[teamA] > 0 && lose[teamB] > 0) {
			win[teamA]--;
			lose[teamB]--;
			if(dfs(idx + 1))  // 현재 게임의 결과를 계속 이어나갔을 때 이후 모든 결과가 문제없으면 true
				return true;
			win[teamA]++;
			lose[teamB]++;
		}
		// b팀이 이기는 경우
		if(win[teamB] > 0 && lose[teamA] > 0) {
			win[teamB]--;
			lose[teamA]--;
			if(dfs(idx + 1))  // 현재 게임의 결과를 계속 이어나갔을 때 이후 모든 결과가 문제없으면 true
				return true;
			win[teamB]++;
			lose[teamA]++;
		}
		// 비기는 경우
		if(draw[teamA] > 0 && draw[teamB] > 0) {
			draw[teamA]--;
			draw[teamB]--;
			if(dfs(idx + 1))  // 현재 게임의 결과를 계속 이어나갔을 때 이후 모든 결과가 문제없으면 true
				return true;
			draw[teamA]++;
			draw[teamB]++;
		}
		return false;
	}

}
