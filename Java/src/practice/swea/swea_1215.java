package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_1215 {
	static int answer;
	static int n, l, t, k; // n은 음식의 수, l은 최대 칼로리, t는 맛, k는 해당 재료 칼로리
	static int[][] arr;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc < t + 1; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			l = Integer.parseInt(st.nextToken());
			answer = 0;

			arr = new int[n][2];
			for(int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				arr[i][0] = Integer.parseInt(st.nextToken());
				arr[i][1] = Integer.parseInt(st.nextToken());
			}
			search(0, 0, 0);
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.print(sb);
	}
	
	static void search(int score, int calrorie, int idx) {
		if(calrorie > l)
			return;
		if(idx == n) {
			answer = score > answer ? score : answer;
			return;
		}
		search(score + arr[idx][0], calrorie + arr[idx][1], idx + 1);
		search(score, calrorie, idx + 1);
	}

}
