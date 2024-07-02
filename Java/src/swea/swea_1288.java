package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class swea_1288 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static int t, n;

	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		int all_number = (1 << 10) - 1; // 0 ~ 9를 모두 표현하는 방법: 111111111

		for (int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			int k = 1;
			int check = 0; // 물리적으로는 0 하나지만 논리적으로는 000000000
			while (check != all_number) { // 모든 비트르 다 찾을 때까지
				char[] split_num = String.valueOf(n * k++).toCharArray(); // 계산된 값을 배열로 변환, 파이썬의 list(str(n*k))
				for (char c : split_num) {
					int num = c - '0'; // 문자열 상태의 숫자를 원래 숫자로 변환
					check = check | (1 << num); // 나온 숫자만큼 비트를 밀어 해당 자리의 비트를 체크
				}
			}
			sb.append("#").append(tc).append(" ").append(n * (k - 1)).append("\n"); // 조건이 만족되는 시점 직전에 k값이 한 번 더 올라가므로
		}
		System.out.println(sb);
	}
}
