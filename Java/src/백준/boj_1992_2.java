package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 분할정복
// bottom up;
public class boj_1992_2 {
	static int n;
	static char[][] map;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new char[n][];
		
		for (int i = 0; i < n; i++) {
			String str = br.readLine();
			map[i] = str.toCharArray();
		}
		
		// 풀이
		System.out.println(divide(0, 0, n));
	}

	static String divide(int y, int x, int n) {
		if(n == 1)
			return String.valueOf(map[y][x]);
		// 네 영역을 모두 조사해서(재귀호출) 모두가 같은지 다른지 처리
		int half = n / 2;
		String ret1 = divide(y, x, half);
		String ret2 = divide(y, x + half, half);
		String ret3 = divide(y + half, x, half);
		String ret4 = divide(y + half, x + half, half);
		
		if(ret1.length() == 1 && ret1.equals(ret2) && ret1.equals(ret3) && ret1.equals(ret4))
			return ret1;
		else {
			StringBuilder sb = new StringBuilder();
			sb.append("(").append(ret1).append(ret2).append(ret3).append(ret4).append(")");
			return sb.toString();
		}
/*  판별하는 조건문에 ret1.length() == 1를 넣어야 하는 이유
아래와 같은 입력이 주어졌을 때 4분할이 아닌 하나의 분할로 인식되기 때문,  ret1.length() == 1: 순수 단일값으로 이루어진 경우
8
00110011
00110011
00110011
00110011
00110011
00110011
00110011
00110011
*/
	}

}
