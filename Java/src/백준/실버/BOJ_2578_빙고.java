package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BOJ_2578_빙고 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] board = new int[5][5];
	static int[] step = new int[26];
	static boolean[][] bingo = new boolean[5][5];
	static HashMap<Integer, int[]> pos = new HashMap<>();
	
	public static void main(String[] args) throws IOException {
		init();
		solve();
	}
	
	static void init() throws IOException {
		for(int i = 0; i < 5; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < 5; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				pos.put(board[i][j], new int[] {i, j});
			}
		}
		
		for(int i = 0; i < 25; i+=5) {
			st = new StringTokenizer(br.readLine());
			for(int j = 1; j < 6; j++)
				step[i + j] = Integer.parseInt(st.nextToken());
		}
	}
	
	static int check() {
		int line = 0;
		
		for(int i = 0; i < 5; i ++)
			if(bingo[i][0] == bingo[i][1] && bingo[i][1] == bingo[i][2] && bingo[i][2] == bingo[i][3] && bingo[i][3] == bingo[i][4] && bingo[i][4] == true)
				line++;
		
		for(int i = 0; i < 5; i ++)
			if(bingo[0][i] == bingo[1][i] && bingo[1][i] == bingo[2][i] && bingo[2][i] == bingo[3][i] && bingo[3][i] == bingo[4][i] && bingo[4][i] == true)
				line++;
		
		if(bingo[0][0] == bingo[1][1] && bingo[1][1] == bingo[2][2] && bingo[2][2] == bingo[3][3] && bingo[3][3] == bingo[4][4] && bingo[4][4] == true)
			line++;
		
		if(bingo[0][4] == bingo[1][3] && bingo[1][3] == bingo[2][2] && bingo[2][2] == bingo[3][1] && bingo[3][1] == bingo[4][0] && bingo[4][0] == true)
			line++;
		
		return line;
	}
	
	static void solve() {
		for (int i = 1; i < 26; i++) {
			int[] current_step = pos.get(step[i]);
			bingo[current_step[0]][current_step[1]] = true;
			
			if(check() >= 3) {
				System.out.println(i);
				break;
			}
		}
	}
}
