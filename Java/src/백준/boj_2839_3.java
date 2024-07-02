package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// dp
public class boj_2839_3 {
	static int n;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		int[] arr = new int[5001];
		Arrays.fill(arr, 5000);
		arr[3] = 1;
		arr[5] = 1;
		
		for(int i = 6; i < n + 1; i++)
			arr[i] = Math.min(arr[i - 3], arr[i - 5]) + 1;
		System.out.println(arr[n] >= 5000 ? -1 : arr[n]);
	}
}