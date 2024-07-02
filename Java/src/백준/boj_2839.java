package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 완탐 - 시간 초과
public class boj_2839 {
	static int n, min;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		min = 5000;
		dfs(0, 0);
		
		min = min == 5000 ? -1 : min;
		System.out.println(min);
	}
	
	static void dfs(int five, int three) {
		int sum = five * 5 + three * 3;
		
		if(sum == n) {
			min = Math.min(min, five + three);
			return;
		}
		else if(sum > n)
			return;
		
		dfs(five + 1, three);  // 현재보다 5kg 하나 더 사용
		dfs(five, three + 1);  // 현재보다 3kg 하나 더 사용
	}
}
