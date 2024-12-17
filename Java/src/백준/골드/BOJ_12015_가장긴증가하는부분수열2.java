package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_12015_가장긴증가하는부분수열2 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[] a;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		a = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(st.nextToken());
		}

		solve();
	}
	
	static int binary_search(int target, int size, int[] lis) {
		int low = 0;
		int high = size;
		int mid = 0;
		
		while(low < high) {
			mid = (low + high) / 2;
			if(lis[mid] < target) {
				low = mid + 1;
			} else {
				high = mid;
			}
		}
		
		return low;
	}
	
	static void solve() {
		int[] lis = new int[n];
		lis[0] = a[0];
		int size = 1;
		
		for(int i = 1; i < n; i++) {
			if(lis[size - 1] < a[i]) {
				size++;
				lis[size - 1] = a[i];
			} else {
				int idx = binary_search(a[i], size, lis);
				lis[idx] = a[i];
			}
		}

		System.out.println(size);
	}
}
