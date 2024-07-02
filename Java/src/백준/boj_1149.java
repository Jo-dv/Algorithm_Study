package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_1149 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[][] cost;
	static int[][] arr;
	static int answer;
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		cost = new int[n][3];
		arr = new int[n][3];
		answer = 0;
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < 3; j++)
				cost[i][j] = Integer.parseInt(st.nextToken());
			arr[i] = cost[i].clone();
		}
		
		for(int i = 1; i < n; i++) {
			for(int j = 0; j < 3; j++) {
				if(j == 0)
					arr[i][j] += Math.min(arr[i - 1][1], arr[i - 1][2]);
				else if(j == 1)
					arr[i][j] += Math.min(arr[i - 1][0], arr[i - 1][2]);
				else
					arr[i][j] += Math.min(arr[i - 1][0], arr[i - 1][1]);
			}
		}
		System.out.println(Math.min(Math.min(arr[n-1][0], arr[n-1][1]), arr[n-1][2]));
	}
}
