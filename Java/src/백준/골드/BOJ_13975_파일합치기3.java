package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_13975_파일합치기3 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int t;
	static int k;
	static long[] data;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		for(int tc = 0; tc < t; tc++) {
			k = Integer.parseInt(br.readLine());
			data = new long[k];
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i < k; i++)
				data[i] = Integer.parseInt(st.nextToken());
			solve();
		}
		System.out.println(sb);
	}
	
	static void solve() {
		long answer = 0;
		PriorityQueue<Long> pq = new PriorityQueue<>();
		for(long i: data)
			pq.add(i);
		
		while(pq.size() > 1) {
			long c1 = pq.poll();
			long c2 = pq.poll();
			answer += (c1 + c2);
			pq.add(c1 + c2);
		}
		sb.append(answer).append("\n");
	}
}
