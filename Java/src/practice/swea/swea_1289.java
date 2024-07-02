package practice.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class swea_1289 {

	static int T, count;
	static char[] input;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {

			count = 0;
			char current = '0'; // 시작은 초기화 값으로

			input = br.readLine().toCharArray();

			int cnt = input.length;
			for (int i = 0; i < cnt; i++) {

				if (input[i] != current) { // 다르면
					count++; // 변경 횟수 증가
				}

				current = input[i];
			}

			sb.append("#").append(t).append(" ").append(count).append("\n");
		}
		System.out.println(sb);
	}
	
	// 반복적인 작업 중 동일한 로직의 처리와 변경되는 조건
	// 반복되는 동일한 로직은 -> 현재 index의 입력 문자와 current문자를 비교해서 다르면 count 증가
	// 변경되는 조건(index 변화, current 문자 변경)
	static void next() {
		
	}
}