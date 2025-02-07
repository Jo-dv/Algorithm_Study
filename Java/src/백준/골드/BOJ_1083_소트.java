package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1083_소트 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[] arr;
	static int s;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		s = Integer.parseInt(br.readLine());

		solve();
	}

	static void solve() {
		for (int i = 0; i < n; i++) {
			if(s == 0) {
				break;
			}
			
			int maxNum = 0;
			int maxIdx = 0;
			for(int j = i; j < i + s + 1; j++) {
				if(maxNum < arr[j]) {
					maxNum = arr[j];
					maxIdx = j;
				}
			}
			
			while(maxIdx != i && s > 0) {  // 최대값이 자기 자신이 아닐 때
				int temp = arr[maxIdx - 1];
				arr[maxIdx - 1] = arr[maxIdx];
				arr[maxIdx] = temp;
				maxIdx--;
				s--;
			}
		}

		for (int i : arr) {
			sb.append(i).append(" ");
		}
		
		System.out.println(sb);
	}
}
