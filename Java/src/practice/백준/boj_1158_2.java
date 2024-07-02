package practice.boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

// 배열 자료구조
public class boj_1158_2 {

	static int N, K;
	static Queue<Integer> queue = new ArrayDeque<Integer>();
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		// 살아있는 사람 전체를 큐에 저장
		for (int i = 1; i <= N; i++) {
			queue.offer(i); // 사람 번호
		}

		// 풀이
		// 죽으면 0 으로
		// 1, 2, 3, 4, 5, 6, 7
		int aliveCnt = 1; // 1부터 시작해서 살아있는 번호에서만 증가

		sb.append("<");
		while (!queue.isEmpty()) {
			int num = queue.poll();
			if(aliveCnt % K == 0)
				sb.append(num).append(", ");
			else
				queue.offer(num);
			aliveCnt++;
		}

		sb.setLength(sb.length() - 2);
		sb.append(">");
		System.out.println(sb);
	}
}