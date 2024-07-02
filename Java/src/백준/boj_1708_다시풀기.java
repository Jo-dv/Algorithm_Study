package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class boj_1708_다시풀기 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static long sx, sy;  // 시작 좌표
	static Node[] arr;
	static int answer;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());

		arr = new Node[n];
		answer = 0;
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			long x = Long.parseLong(st.nextToken());
			long y = Long.parseLong(st.nextToken());
			arr[i] = new Node(x, y);
			if(i == 0) {
				sx = x;
				sy = y;
			}
			if(sy > y) {
				sx = x;
				sy = y;
			}
			else if(sy == y && sx > x) {
				sx = x;
				sy = y;
			}
		}
		
		Arrays.sort(arr, (p1, p2) -> {
			int result = ccw(new Node(sx, sy), p1, p2);
			if(result > 0)
				return -1;
			else if(result < 0)
				return 1;
			else {
				long diff = distance(sx, sy, p1.x, p1.y) - distance(sx, sy, p2.x, p2.y);
				return diff > 0 ? 1 : -1; // p1이 더 멀리있으면 1 -> 더 뒤로 가도록
			}
		});
		
		Stack<Node> stack = new Stack<>();
		stack.add(new Node(sx, sy));
		
		int len = arr.length;
		for(int i = 1; i < len; i++) {
			Node next = arr[i];
			
			while(stack.size() > 1) {
				Node first = stack.get(stack.size() - 2);
				Node second = stack.get(stack.size() - 1);
				int result = ccw(first, second, next);
				if(result <= 0)
					stack.pop();
			}
			stack.add(arr[i]);
		}
		System.out.println(stack.size());
	}
	
	static void solve(int i) {
		long result = ccw(arr[i], arr[i+1], arr[i+2]);
		if(result > 0)
			System.out.println(1);
		else if(result < 0)
			System.out.println(-1);
		else
			System.out.println(0);
	}
	
	static int ccw(Node a, Node b, Node c) {
		long result = (b.x - a.x) * (c.y - b.y) - (b.y - a.y) * (c.x - b.x);
		if(result > 0)  // 반시계
			return 1;
		else if(result < 0)  // 시계
			return -1;
		else
			return 0;
	}
	
	static long distance(long x1, long y1, long x2, long y2) {
		return (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2);
	}
	
	static class Node {
		long x, y;

		public Node(long x, long y) {
			this.x = x;
			this.y = y;
		}
	}
}
