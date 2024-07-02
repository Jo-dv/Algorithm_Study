package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class swea_5656 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int t;
	static int n, w, h;
	static int[][] board;
	static int[][] init_board;
	static int[] fall_pos;
	static int answer;
	static Deque<Node> q;
	static int[][] direction = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());
			board = new int[h][w];
			init_board = new int[h][w];
			fall_pos = new int[n]; // 구슬을 떨어뜨릴 위치를 기록할 배열
			answer = Integer.MAX_VALUE;
			for (int i = 0; i < h; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < w; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
					init_board[i][j] = board[i][j]; // 게임을 초기화할 때 사용될 원본 배열
				}
			}
			makeGame(0);
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}

	static void makeGame(int bead_num) { // 구슬을 떨어뜨릴 위치 초기화 후 게임 시작
		if (bead_num == n) {
			startGame();
			clearGame(); // 다음 게임을 위해서 파괴된 벽돌 재생성
			return;
		}
		for (int i = 0; i < w; i++) {
			fall_pos[bead_num] = i;
			makeGame(bead_num + 1);
		}
	}

	static void startGame() { // 주어진 구슬 위치들을 가지고 게임 시작
		int y = h - 1; // 더 이상 부술 벽이 없을 경우 y는 바닥을 가리킴 -> 부술 벽이 없는 상태를 상정
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < h; j++) {
				if (board[j][fall_pos[i]] != 0) {
					y = j; // 해당 라인에서 첫 벽돌 마주
					break;
				}
			}
			clearBrick(y, fall_pos[i]); // 해당 위치부터 벽돌 부수기 시작
			moveBrick(); // 부숴진 벽돌들 사이로 남은 벽돌 이동
			getScore(); // 이동 종료 후, 남은 벽돌의 수 계산
		}
	}

	static void clearBrick(int sy, int sx) {
		q = new ArrayDeque<>();
		q.offer(new Node(sy, sx, board[sy][sx])); // y, x 해당 벽돌의 파괴 범위
		board[sy][sx] = 0; // 범위랑 상관없이 해당 벽돌은 바로 제거

		while (!q.isEmpty()) {
			Node current = q.poll();
			for (int i = 1; i < current.range; i++) { // 최소 세기는 1부터이며 해당 벽돌에 새겨진 범위 -1 까지만 적용
				for (int[] d : direction) {
					int my = current.y + (d[0] * i);
					int mx = current.x + (d[1] * i);
					if (0 <= my && my < h && 0 <= mx && mx < w && board[my][mx] != 0) {
						q.add(new Node(my, mx, board[my][mx])); // 인접 범위의 벽돌 삽입
						board[my][mx] = 0; // 벽돌 제거
					}
				}
			}
		}
	}

	static void moveBrick() {
		q = new ArrayDeque<>();
		for (int i = 0; i < w; i++) {
			for (int j = 0; j < h; j++)
				if (board[j][i] != 0)
					q.offer(new Node(j, i, board[j][i])); // 파괴되고 남은 벽돌 삽입
			for (int j = h - 1; j >= 0; j--) { // 큐의 뒤에서부터 값을 가져와 밑에서부터 순차적으로 채움
				if (!q.isEmpty()) { // 옮기는 작업
					Node current = q.pollLast();
					board[j][i] = current.range;
				} else
					board[j][i] = 0;
			}
		}
	}

	static void getScore() {
		int score = 0;
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				if (board[i][j] > 0)
					score++;
		answer = Math.min(score, answer);
	}

	static void clearGame() { // 게임 초기화 -> 벽돌 재생성
		for (int i = 0; i < h; i++)
			board[i] = init_board[i].clone();
	}

	static class Node {
		int y, x, range;

		public Node(int y, int x, int range) {
			this.y = y;
			this.x = x;
			this.range = range;
		}
	}
}
