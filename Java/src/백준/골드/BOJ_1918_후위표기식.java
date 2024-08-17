package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ_1918_후위표기식 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static Stack<Character> stack = new Stack<>();
	static String infix;
	static StringBuilder answer = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		infix = br.readLine();
		
		for(char data: infix.toCharArray()) {
			if(data == '(') 
				stack.add(data);
			else if(data == ')') {
				while(!stack.isEmpty() && stack.peek() != '(') 
					answer.append(stack.pop());
				stack.pop();
			}
			else if(data == '*' || data == '/') {
				while(!stack.isEmpty() && (stack.peek() == '*' || stack.peek() == '/'))  // 동등한 우선 순위는 순차적으로 계산 A*B*C -> AB*C*
					answer.append(stack.pop());
				stack.add(data);
			}
			else if(data == '+' || data == '-') {
				while(!stack.isEmpty() && stack.peek() != '(')
					answer.append(stack.pop());
				stack.add(data);
			}
			else
				answer.append(data);
		}
		
		while(!stack.isEmpty())
			answer.append(stack.pop());
		
		System.out.println(answer);
	}
}
