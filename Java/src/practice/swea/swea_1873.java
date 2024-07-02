package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class swea_1873 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		int[][] d_vectors = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
		HashMap<Character, int[]> direction = new HashMap<Character, int[]>() {
			{
				put('U', new int[] { -1, 0 });
				put('D', new int[] { 1, 0 });
				put('L', new int[] { 0, -1 });
				put('R', new int[] { 0, 1 });
			}
		};

		HashMap<Character, Character> tank_direction = new HashMap<Character, Character>() {
			{
				put('U', '^');
				put('D', 'v');
				put('L', '<');
				put('R', '>');
			}
		};
		List<Character> tank = Arrays.asList('^', 'v', '<', '>');

		for (int tc = 1; tc < t + 1; tc++) {
			st = new StringTokenizer(br.readLine());
			int h = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			char[][] maps = new char[h][w];
			for (int i = 0; i < h; i++)
				maps[i] = br.readLine().toCharArray();
			int n = Integer.parseInt(br.readLine());
			char[] cs = br.readLine().toCharArray();
			int y = 0, x = 0, tk = 0;
			int[] d = null;

			for (int col = 0; col < h; col++) {  // 탱크 위치 탐색
				for (int row = 0; row < w; row++) {
					if (tank.contains(maps[col][row])) {
						y = col;
						x = row;
						tk = tank.indexOf(maps[y][x]);  // 현재 탱크의 모양
						d = d_vectors[tk];  // 탱크 모양에 따른 방향 벡터 저장
						break;
					}
				}
			}

			for (char c : cs) {  // 명령어 탐색
				if (c != 'S') {  // 이동 명령어라면
					d = direction.get(c);  // 명령어에 따른 방향 벡터 저장
					int my = d[0], mx = d[1];  // 이동할 좌표
					maps[y][x] = tank_direction.get(c);  // 방향에 맞춰 탱크 회전
					if (0 <= y + my && y + my < h && 0 <= x + mx && x + mx < w && maps[y + my][x + mx] == '.') {  // 이동할 좌표가 유효 범위이면서 평지라면
						maps[y + my][x + mx] = maps[y][x];  // 탱크 이동
						maps[y][x] = '.';  // 이동한 자리는 평지로 변경
						y += my;  // 탱크의 현재 좌표 갱신
						x += mx;
					}
				}
				else {  // 발사 명령어라면
					int sy = y, sx = x;  // 미사일은 탱크에서부터 발사되므로 현재 탱크의 위치 저장
					int my = d[0], mx = d[1];  // 미사일이 이동할 좌표, 탱크에 방향에 따름
					while (0 <= sy + my && sy + my < h && 0 <= sx + mx && sx + mx < w) {  // 이동할 좌표가 유효 범위를 벗어나기 전까지
						if (maps[sy + my][sx + mx] == '#')  // 이동할 좌표에 강철벽이 있다면
							break;  // 그대로 종료
						if (maps[sy + my][sx + mx] == '*') {  // 벽돌벽이라면
							maps[sy + my][sx + mx] = '.';  // 파괴
							break;  // 파괴 후 종료
						}
						sy += my;  // 미사일 이동
						sx += mx;
					}
				}
			}
			System.out.printf("#%d ", tc);
			for (char[] answer : maps) {
				System.out.println(String.valueOf(answer));  // 문자 배열을 문자열로
			}
		}
	}
}