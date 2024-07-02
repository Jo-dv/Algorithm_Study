package swea;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_1210 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[][] ladder = new int[100][100];
		int[][] direction = { { -1, 0 }, { 0, -1 }, { 0, 1 } }; // 방향 벡터 정의
		int d = 0;
		for (int t = 1; t < 11; t++) {
			int y = 99; // 새로운 테스트 케이스를 받을 때마다 초기화, 변수 초기화가 제대로 이루어지는지 항상 확인할 것
			int x = 0;
			br.readLine(); // 의미없는 test input;
			for (int col = 0; col < 100; col++) { // 초기화
				st = new StringTokenizer(br.readLine());
				for (int row = 0; row < 100; row++)
					ladder[col][row] = Integer.parseInt(st.nextToken());
			}

			for (int row = 0; row < 100; row++) // 시작 위치 탐색
				if (ladder[99][row] == 2)
					x = row;

			while (y != 0) { // 위에 도달할 때까지
				if (-1 < x - 1 && ladder[y][x - 1] == 1) { // 유효 범위이며 왼쪽으로 이동할 수 있다면
					d = 1;
					while (-1 < x - 1 && ladder[y + direction[d][0]][x + direction[d][1]] == 1) { // 유효 범위이며 왼쪽으로 이동이 다
																									// 될 때까지
						y += direction[d][0];
						x += direction[d][1];
					}
				} else if (x + 1 < 100 && ladder[y][x + 1] == 1) { // 유효 범위이며 오른쪽으로 이동할 수 있다면
					d = 2;
					while (x + 1 < 100 && ladder[y + direction[d][0]][x + direction[d][1]] == 1) { // 유효 범위이며 오른쪽으로 이동이
																									// 다 될 때까지
						y += direction[d][0];
						x += direction[d][1];
					}
				} // if - else if를 사용해서 한 조건만 만족되면 다른 조건은 검사하지 않도록 처리
				d = 0; // 조건문이 처리되지 않는다면 위로 이동
				y += direction[d][0];
				x += direction[d][1];
			}
			System.out.printf("#%d %d\n", t, x);
		}
	}
}