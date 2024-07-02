package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/*
1
5
1 3 2 5 4

 */
public class swea_3307_2 {
	static int n, T, len;
	static int[] input;
	static int[] memo;
	// memo[2] = 5;의 의미는 (2 + 1) 길이가 3인 lis를 만드는 가장 작은 수
	// pos index 변수
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		
		for(int t = 1; t <= T; t++) {
			n = Integer.parseInt(br.readLine());
			input = new int[n];
			memo = new int[n];
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i = 0; i < n; i++)
				input[i] = Integer.parseInt(st.nextToken());
			
			// 풀이
			len = 0;
			for(int i = 0; i < n; i++) {
				int pos = Arrays.binarySearch(memo, 0, len, input[i]);
				if(pos >= 0)
					continue;
				// 음수일 때 -> 갱신 -> 음수가 반환되었다는 것은 값이 없다는 것을 의미, -2: -(들어갈 인덱스 + 1)
				// 음수를 양수로 변환
				pos = Math.abs(pos) - 1; // 위치 값 보정
				memo[pos] = input[i];
				if(len == pos)
					len++;  // lis 증가
			}
			sb.append("#").append(t).append(" ").append(len).append("\n");
		}
		System.out.println(sb);
	}
}
