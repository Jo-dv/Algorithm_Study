package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_11659 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		
		int[][] range = new int[m][2];
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			range[i][0] = Integer.parseInt(st.nextToken()) - 1;
			range[i][1] = Integer.parseInt(st.nextToken()) - 1;
		}
		
		int[] acc = new int[n];
		acc[0] = arr[0];
		for(int i = 1; i < n; i++) {
			acc[i] = arr[i] + arr[i-1];
			System.out.print(arr[i] + " ");
			System.out.println(acc[i]);
		}
		
		System.out.println(Arrays.toString(acc));
//		for (int[] r : range) {
//			int sum = 0;
//			for(int s = r[0]; s <= r[1]; s++)
//				sum += arr[s];
//			System.out.println(sum);
//		}
		
	}
}
