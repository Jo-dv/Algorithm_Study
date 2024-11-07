package 백준.골드;

import java.util.*;
import java.io.*;

public class BOJ_13913_숨바꼭질4 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, k;
	static int[] time;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		solve();
	}
	
	static void print_result(int[] trace, int current) {
		Stack<Integer> result = new Stack<>();
		result.add(k);
		
		while(true) {
			current = trace[current];
			result.push(current);
			if(current == n)
				break;	
		}
		
		System.out.println(time[k]);
		while(!result.isEmpty())
			System.out.print(result.pop() + " ");
	}
	
	static void solve() {
		time = new int[100001];
		Queue<Integer> q = new ArrayDeque<>();
		int[] trace = new int[100001];
		q.add(n);
		
		if (n == k) { // 시작점과 목표가 같을 때
            System.out.println(0);
            System.out.println(n);
            return;
        }

		while(!q.isEmpty()) {
			int current = q.poll();
			
			for(int i: new int[] {current - 1, current + 1, current * 2}) {
				if(0 <= i && i <= 100000 && time[i] == 0) {
					time[i] = time[current] + 1;
					q.add(i);
					trace[i] = current;
					
					if(i == k) 
						print_result(trace, i);
				}
			}
		}
	}
}