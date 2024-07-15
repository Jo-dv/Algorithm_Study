package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_20040_사이클게임 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static Point[] points;
	static int[] parent;
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		points = new Point[m];
		parent = new int[n];
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			points[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		}
		
		solve();
	}
	
	static void init_parent() {
		for(int i = 0; i < n; i++)
			parent[i] = i;
	}
	
	static int find(int x) {
		if(parent[x] == x)
			return x;
		return parent[x] = find(parent[x]);
	}
	
	static boolean union(int x, int y) {
		x = find(x);
		y = find(y);
		
		if(x == y)
			return false;
		parent[y] = x;
		return true;
	}
	
	static void solve() {
		boolean flag = false;
		init_parent();
		
		for(Point game: points)  // 게임 진행
			if(union(game.point1, game.point2))  // 결합이 이루어졌다면 아직 사이클이 만들어지지 않음
				answer++;
			else {  // 더 이상 결합을 이룰 수 없으면 사이클이 만들어진 것
				System.out.println(++answer);  // 답을 갱신하는 것은 결합이 안 됐을 때만 수행되므로 마지막 출력에 최종 게임 진행 반영
				flag = true;  // 게임 종료 플래그
				break;
			}
		
		if(!flag)  // 플래그가 활성화 되지 않았다면 게임이 종료됐음에도 사이클이 만들어지지 않았다는 의미
			System.out.println(0);
	}
	
	static class Point {
		int point1, point2;

		public Point(int point1, int point2) {
			this.point1 = point1;
			this.point2 = point2;
		}
	}
}
