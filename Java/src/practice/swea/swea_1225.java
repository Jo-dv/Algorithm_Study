package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class swea_1225 {

	static Queue<Integer> queue = new ArrayDeque<Integer>();
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			String t = br.readLine();
			if(t == null || t.length() == 0)
				break;
			queue.clear();
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 8; i++) {
				queue.offer(Integer.parseInt(st.nextToken()));
			}
			solve();
			sb.append("#").append(t).append(" ");
			for (int num : queue) {
				sb.append(num).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
	static void solve() {
		int num = 0;
		while(true) {
			for (int i = 1; i < 6; i++) {
				num = queue.poll() - i;
				if(num <= 0) {
					queue.offer(0);
					return;
				}
				queue.offer(num);
			}
		}
	}
}
