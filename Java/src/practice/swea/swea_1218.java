package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class swea_1218 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for(int tc = 1; tc < 11; tc++) {
			int n = Integer.parseInt(br.readLine());
			char check;
			char c;
			int answer = 1;
			Deque<Character> stack = new ArrayDeque<>();
			String in_str = br.readLine();
			
			for (int i = 0; i < n; i++) {
				c = in_str.charAt(i);
				if (c == '(' || c == '[' || c == '{' || c == '<')
					stack.addLast(c);
				else {
					if(!stack.isEmpty()) {
						check = stack.pollLast();
						if((check == '(' && c != ')') || (check == '[' && c != ']') || (check == '{' && c != '}') || (check == '<' && c != '>')) {
							answer = 0;
							break;
						}
					}
					else {
						answer = 0;
						break;
					}
				}
			}
			System.out.printf("#%d %d\n", tc, (!stack.isEmpty()) ? 0 : answer);
		}

	}

}
