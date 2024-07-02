package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class boj_6198 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int answer = 0;
		Deque<Integer> q = new ArrayDeque<Integer>();
		Deque<Integer> value = new ArrayDeque<Integer>();
		
		for(int i = 0; i <= n; i++) {
			int height = Integer.parseInt(br.readLine());
			while(!q.isEmpty()) {
				if(q.peekLast() > height) {
					answer += 1;
				}
			}
			q.addLast(height);
		}
	}
}
