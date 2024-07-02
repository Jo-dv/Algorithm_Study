package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 분할정복이긴한데
// 전체 -> 부분 -> top down;
public class boj_1992 {
	static int n;
	static char[][] map;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new char[n][];
		
		for (int i = 0; i < n; i++) {
			String str = br.readLine();
			map[i] = str.toCharArray();
		}
		
		// 풀이
		divide(0, 0, n);
		System.out.println(sb);
	}
	
	static boolean check(int y, int x, int n) {
		char ch = map[y][x];
		for (int i = y; i < y + n; i++) {
			for (int j = x; j < x + n; j++) {
				if(ch != map[i][j])
					return false;
			}
		}
		sb.append(ch);
		return true;
	}
	
	static void divide(int y, int x, int n) {
		// check() -> true/false 구분
		if(!check(y, x, n)) {
			// () + 4분할 결과
			// 너비를 반으로 줄인다.
			int half = n / 2;
			
			sb.append("(");
			divide(y, x, half);
			divide(y, x + half, half);
			divide(y + half, x, half);
			divide(y + half, x + half, half);
			sb.append(")");
		}
	}

}
