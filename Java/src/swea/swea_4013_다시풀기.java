package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_4013_다시풀기 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuffer sb = new StringBuffer();
	static StringTokenizer st;
	static int t, k;
	static int[][] magnet;
	static Node[] rotation_info;
	static int[] dir;
	static int[] score = { 1, 2, 4, 8 };
	static int answer;

	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			k = Integer.parseInt(br.readLine());
			magnet = new int[4][8];
			rotation_info = new Node[k];
			answer = 0;

			for (int i = 0; i < 4; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 8; j++)
					magnet[i][j] = Integer.parseInt(st.nextToken());
			}
			for (int i = 0; i < k; i++) {
				st = new StringTokenizer(br.readLine());
				rotation_info[i] = new Node(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()));
				check(rotation_info[i].num, rotation_info[i].dir);
				rotate();
			}

			for (int i = 0; i < 4; i++)
				if (magnet[i][0] == 1)
					answer += score[i];
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}

	static void check(int n, int d) {
		dir = new int[4]; // 회전 정보
		dir[n] = d;

		// 회전하는 자석은 탐색에서 제외
		for (int i = n + 1; i < 4; i++) { // 오른쪽 검사
			if (magnet[i - 1][2] != magnet[i][6])
				dir[i] = dir[i - 1] * -1;
		}

		for (int i = n - 1; i >= 0; i--) { // 왼쪽 검사
			if (magnet[i][2] != magnet[i + 1][6])
				dir[i] = dir[i + 1] * -1;
		}
	}

	static void rotate() {
		for (int i = 0; i < 4; i++) {
			int temp;
			// 각 자석별 회전 방향에 따라 회전
			switch (dir[i]) {
			case 1: // 시계 방향
				temp = magnet[i][7];
				for (int j = 7; j > 0; j--) {
					magnet[i][j] = magnet[i][j - 1];
				}
				magnet[i][0] = temp;
				break;
			case -1: // 반시계 방향
				temp = magnet[i][0];
				for (int j = 0; j < 7; j++) {
					magnet[i][j] = magnet[i][j + 1];
				}
				magnet[i][7] = temp;
				break;
			default:
				break;
			}
		}
	}

	static class Node {
		int num, dir;

		public Node(int num, int dir) {
			this.num = num;
			this.dir = dir;
		}
	}
}
