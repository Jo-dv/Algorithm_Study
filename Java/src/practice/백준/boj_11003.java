package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class boj_11003 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int n, l;
	static int[] arr;
	static ArrayDeque<Node> dq = new ArrayDeque<>();
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		arr = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		
		for(int i = 0; i < n; i++) {
			if(!dq.isEmpty() && dq.peek().idx <= i-l)  // 0번부터 시작하므로 +1 해줄 필요 없음
				dq.pollFirst();  //  i ≤ 0 인 A는 무시한다는 조건 하에 그 다음부터 앞에서부터 값 제거
			
			while(!dq.isEmpty() && arr[i] < dq.peekLast().val) {
				dq.pollLast();  // 들어오려는 값이 마지막 값보다 작다면 마지막 값 제거, 항상 최소가 유지되게
			}
			dq.add(new Node(i, arr[i]));
			sb.append(dq.peek().val).append(" ");
		}
		System.out.println(sb);
	}
	
	static class Node {
		int idx, val;

		public Node(int idx, int val) {
			super();
			this.idx = idx;
			this.val = val;
		}
	}
}
