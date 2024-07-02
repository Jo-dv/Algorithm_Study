package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_9229 {
	static int n, m;
	static int[] weights;
	static int[] subset;
	static StringBuilder sb = new StringBuilder();
	static int answer;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int tc = Integer.parseInt(br.readLine());
		
		for(int t = 1; t <= tc; t++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			weights = new int[n];
			subset = new int[2];
			answer = -1;
			
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i < n; i++) {
				weights[i] = Integer.parseInt(st.nextToken());
			}
			search(0, 0);
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
	
	static void search(int idx, int target) {
		if(target == 2) {
			int sum = subset[0] + subset[1];
			answer = m >= sum && sum > answer ? sum : answer;
			return;
		}
		if(idx == n)
			return;
		subset[target] = weights[idx];
		search(idx + 1, target + 1);
		search(idx + 1, target);
	}
}
