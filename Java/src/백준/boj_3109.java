package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_3109 {
	static boolean[][] check;
	static char[][] grid;
	static int r;
	static int c;
	static int answer = 0;
	static boolean flag;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		grid = new char[r][c];
		check = new boolean[r][c];
		
		for(int i = 0; i < r; i++)
			grid[i] = br.readLine().toCharArray();

		for(int i = 0; i < r; i++) {
			flag = false;  // 각 노드마다 도착지점이 다르기 때문에 시작할 때 마다 플래그 초기화
			dfs(i, 0);  /// 시작 위치는 항상 첫 컬럼에서 시작
		}
		
		System.out.println(answer);
	}
	
	static void dfs(int y, int x) {
		if(-1 < y && y < r && -1 < x && x < c && !check[y][x] && grid[y][x] != 'x' && !flag) {  // 유효 범위이며 아직 방문 및 도착을 안 했다면
			check[y][x] = true;  // 방문 처리, 성공하든 실패하든 어쨌든 다음 탐색을 할 필요가 없기에 방문하면 일단 true
			if(x == c - 1) {
				answer++;
				flag = true;  // 각 방향 중 하나라도 도착하면 다른 탐색은 수행할 필요가 없기 때문에 그것을 구별한 플래그를 활성화
			}
			dfs(y - 1, x + 1);  // 주어진 방향에 대해서 탐색
			dfs(y, x + 1);
			dfs(y + 1, x + 1);
		}
		else
			return;
	}
}
