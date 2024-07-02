package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class boj_1158 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		Deque<Integer> deque = new ArrayDeque<Integer>();
		StringBuilder sb = new StringBuilder();
		
		for(int i = 1; i < n + 1; i++)
			deque.add(i);
		
		sb.append("<");
		while(deque.size() != 1) {
			for(int i = 0; i < k - 1; i++)
				deque.addLast(deque.pollFirst());
			sb.append(deque.pollFirst()).append(", ");
		}
		sb.append(deque.pop()).append(">");
		System.out.println(sb);
	}
}
