package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_3055 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char[][] map;
	static boolean[][] visited;
	static Queue<Node> water_area;
	static int r, c;
	static int[][] direction = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
	static Node hedgehog;
	static boolean flag = false;

	// 고슴도치(S)와 물(*)은 X를 통과할 수 없음
	// 고슴도치는 *를 통과할 수 없음
	// 물은 비버의 굴(D)을 통과할 수 없음

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		map = new char[r][c];
		visited = new boolean[r][c];
		water_area = new ArrayDeque<>();
		for (int i = 0; i < r; i++) {
			String col = br.readLine();
			for (int j = 0; j < c; j++) {
				map[i][j] = col.charAt(j);
				if (map[i][j] == 'X')  // 돌은 뭐든 통과할 수 없으므로 처음부터 막아둠
					visited[i][j] = true;
				if (map[i][j] == 'S')
					hedgehog = new Node(i, j, 0);  // 두더지 위치 = 시작
				if (map[i][j] == '*') {  // 두더지와 함께 물의 움직임을 같이 처리해야 하므로 물을 위치를 저장하는 큐를 따로 설정
					visited[i][j] = true;
					water_area.offer(new Node(i, j));
				}
			}
		}
		int answer = bfs();
		System.out.println(answer != -1 ? answer : "KAKTUS");  // 도착하지 못했다면 문자열 출력
	}

	static int bfs() {
		Queue<Node> q = new ArrayDeque<>();
		q.offer(hedgehog);
		visited[hedgehog.y][hedgehog.x] = true;

		while (!q.isEmpty()) {
			flood();  // 물을 먼저 이동 시킨 후 두더지 이동, 그렇지 않으면 두더지를 침수 지역에 보내버리게 됨
			int len = q.size();  // 현재 큐에 저장된 만큼만 처리
			for (int i = 0; i < len; i++) {  // 해당 처리를 하지 않아서 정답 도출에 굉장히 애씀, 큐에 저장되는 것은 다음 시점의 움직임들을 저장, 물은 시점당(현재 큐의 길이만큼) 한 번만 범람해야 함
				// 해당 반복문을 걸지 않으면 물이 시점당 범람하지 않고 움직임이 하나씩 처리될 때마다 범람하게 됨 -> 결과적으로 침수가 더욱 많이 이루어짐
				Node current = q.poll();
				int y = current.y;
				int x = current.x;
				if (map[y][x] == 'D')  // 비버굴에 도착했다면
					return current.step;  // 도착 시점의 걸음 수 반환
				for (int[] d : direction) {  // 네 방향 탐색
					int my = y + d[0];
					int mx = x + d[1];
					if (isValid(my, mx) && !visited[my][mx]) {  // 유효한 범위 내에 아직 방문하지 않은 곳이라면
						q.offer(new Node(my, mx, current.step + 1));
						visited[my][mx] = true;
					}
				}
			}
		}
		return -1;
	}

	static void flood() {
		int len = water_area.size();
		for (int i = 0; i < len; i++) {  // 현재 저장된 침수 정보만큼 -> 그렇지 않으면 인접한 지역은 모두 침수됨 -> 해당 로직은 제대로 작성해놓고 두더지 움직임에는 적용하지 않았던 것이 실패 요소
			Node temp = water_area.poll();
			int y = temp.y;
			int x = temp.x;
			for (int[] d : direction) {
				int my = y + d[0];
				int mx = x + d[1];
				if (isValid(my, mx) && map[my][mx] == '.') {
					map[my][mx] = '*';  // 침수 상태로 바꿔줌 -> 침수는 두더지가 다녀간 곳도 가능하므로 visited의 여부로 판단해서는 안 되고 빈 곳 여부로 판단해야 함
					visited[my][mx] = true;
					water_area.offer(new Node(my, mx));  // 침수된 지역의 위치를 다시 갱신, 여담으로 for each를 사용할 때 사용되는 주체를 수정하면 안 됨 -> 단순 반복문 사용
				}
			}
		}
	}

	static boolean isValid(int y, int x) {  // 유효 범위 확인
		if (0 <= y && y < r && 0 <= x && x < c)
			return true;
		return false;
	}

	static class Node {
		int y, x;
		int step;

		public Node(int y, int x) {  // 물
			this.y = y;
			this.x = x;
		};

		public Node(int y, int x, int step) {  // 두더지
			this.y = y;
			this.x = x;
			this.step = step;
		}
	}
}
