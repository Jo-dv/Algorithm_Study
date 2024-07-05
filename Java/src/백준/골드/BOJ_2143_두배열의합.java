package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_2143_두배열의합 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int t;
	static int n, m;
	static int[] a, b;
	static long answer = 0;
	
	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		
		n = Integer.parseInt(br.readLine());
		a = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++)
			a[i] = Integer.parseInt(st.nextToken());
		
		m = Integer.parseInt(br.readLine());
		b = new int[m];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < m; i++)
			b[i] = Integer.parseInt(st.nextToken());
		
		solve();
	}
	
	static List<Integer> accumulate(int[] arr) {
		List<Integer> acc_array = new ArrayList<>();
		int len = arr.length;
		int sum;
		
		for(int i = 0; i < len; i++) {  // 배열의 각 값에서부터 끝까지의 일련의 누적합 계산
			sum = 0;
			for(int j = i; j < len; j++) {  // i에 대한 누적합 계산
				sum += arr[j];
				acc_array.add(sum);
			}
		}
		
		return acc_array;
	}
	
	static void solve() {
		List<Integer> acc_a = accumulate(a);
		List<Integer> acc_b = accumulate(b);
		
		HashMap<Integer, Integer> hash = new HashMap<>();
		for(Integer num : acc_a)
			hash.put(num, !hash.containsKey(num) ? 1 : hash.get(num) + 1);
		
		for(Integer num: acc_b)
			answer += hash.getOrDefault(t - num, 0);
		
		System.out.println(answer);
		System.out.println(1000000 * 10000000);
	}
}
