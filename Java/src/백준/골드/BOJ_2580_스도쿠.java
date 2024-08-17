package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_2580_스도쿠 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] sudoku = new int[9][9];
	static int[] col_mask = new int[9];
	static int[] row_mask = new int[9];
	static int[] box_mask = new int[9];
	static StringBuilder answer = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		for(int y = 0; y < 9; y++) {
			st = new StringTokenizer(br.readLine());
			for(int x = 0; x < 9; x++)
				sudoku[y][x] = Integer.parseInt(st.nextToken());
		}
		
		solve();
		System.out.println(answer);
	}
	
	static void find_zero(List<Node> zero) {
		for(int y = 0; y < 9; y++)
			for(int x = 0; x < 9; x++)
				if(sudoku[y][x] == 0)
					zero.add(new Node(y, x));			
	}
	
	static void init_mask() {
		for(int y = 0; y < 9; y++)
			for(int x = 0; x < 9; x++)
				if(sudoku[y][x] != 0) {
					int mask = 1 << sudoku[y][x];
					col_mask[y] |= mask;
					row_mask[x] |= mask;
					box_mask[(y / 3) * 3 + (x / 3)] |= mask;
				}
	}
	
	static boolean is_valid(int y, int x, int num) {
		int mask = 1 << num;
		if((col_mask[y] & mask) != 0)
			return false;
		if((row_mask[x] & mask) != 0)
			return false;
		if((box_mask[(y / 3) * 3 + (x / 3)] & mask) != 0)
			return false;
		
		return true;
	}
	
	static void place_num(int y, int x, int num) {
		int mask = 1 << num;
		sudoku[y][x] = num;
		col_mask[y] |= mask;
		row_mask[x] |= mask;
		box_mask[(y / 3) * 3 + (x / 3)] |= mask;
	}
	
	static void remove_num(int y, int x, int num) {
		int mask = ~(1 << num);
		sudoku[y][x] = 0;
		col_mask[y] &= mask;
		row_mask[x] &= mask;
		box_mask[(y / 3) * 3 + (x / 3)] &= mask;
	}
	
	static boolean find_sudoku(List<Node> zero, int zero_cnt) {
		if(zero_cnt == zero.size()) {
			for(int y = 0; y < 9; y++) {
				for(int x = 0; x < 9; x++)
					answer.append(sudoku[y][x]).append(" ");
				answer.append("\n");
			}
			
			return true;
		}
		
		Node current_num = zero.get(zero_cnt);
		
		for(int num = 1; num < 10; num++) {
			if(is_valid(current_num.y, current_num.x, num)) {
				place_num(current_num.y, current_num.x, num);
				if(find_sudoku(zero, zero_cnt + 1))
					return true;
				remove_num(current_num.y, current_num.x, num);
			}
		}
		
		return false;
	}
	
	static void solve() {
		List<Node> zero_pos = new ArrayList<>();
		
		find_zero(zero_pos);
		init_mask();
		find_sudoku(zero_pos, 0);
	}
	
	static class Node {
		int y, x;
		
		Node(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}
}
