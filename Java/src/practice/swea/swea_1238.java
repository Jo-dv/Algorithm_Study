package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class swea_1238 {
	static ArrayList<Integer>[] arr;
	static boolean[] visit;
	static int depth, value;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		for (int t = 1; t <= 10; t++) {
			arr = new ArrayList[101];  // 1 ~ 100을 헤드로 하는 인데스 인접 리스트 구현
			visit = new boolean[101];  // 노드는 1 ~ 100
			depth = 0;
			value = 0;
			st = new StringTokenizer(br.readLine());
			int len = Integer.parseInt(st.nextToken()) / 2;
			int start = Integer.parseInt(st.nextToken());

			for (int i = 0; i < 101; i++)
				arr[i] = new ArrayList<Integer>();

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < len; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				if (!arr[from].contains(to))  // 중복 연결 회피
					arr[from].add(to);
			}
			bfs(start);
			sb.append("#").append(t).append(" ").append(value).append("\n");
		}
		System.out.println(sb);
	}

	static void bfs(int idx) {
		Queue<Node> q = new ArrayDeque<Node>();
		q.add(new Node(idx, 1));  // 입력 노드에서 깊이 1부터 시작
		visit[idx] = true;
		
		while (!q.isEmpty()) {
			Node current = q.poll();
			if (depth <= current.depth) {
				if (depth < current.depth)  // depth가 깊어진 시점에서
					value = 0;  // 해당 depth의 값들 중 큰 값을 찾아야 하므로 기존 value 초기화
				depth = current.depth;
				value = value < current.num ? current.num : value;
			}
			for (int i = 0; i < arr[current.num].size(); i++) {  // 현재 노드와 연결된 노드들을 탐색
				int next = (int) arr[current.num].get(i);
				if(!visit[next]) {  // 아직 방문하지 않았다면 -> 방문 여부를 검사하지 않으면 사이클에 빠짐
					q.add(new Node(next, current.depth + 1));  // 깊이를 갱신해서 다음 탐색할 노드로 추가
					visit[next] = true;
				}
			}
		}
	}

	static class Node {
		int num;
		int depth;

		Node(int num, int depth) {
			this.num = num;
			this.depth = depth;
		}
	}

}