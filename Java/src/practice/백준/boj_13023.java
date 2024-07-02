package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj_13023 {
	static int n, m, answer;
	static ArrayList<Integer>[] graph;
	static boolean[] visit;

	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		graph = new ArrayList[n];
		visit = new boolean[n];
		answer = 0;

		for (int i = 0; i < n; i++)  // 인접 리스트
			graph[i] = new ArrayList<Integer>();

		for (int i = 0; i < m; i++) {  // 리스트 초기화
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph[a].add(b);  // 양방향 연결
			graph[b].add(a);
		}

		for (int i = 0; i < n; i++) {  // a -> b -> c -> d -> e의 관계를 찾는 문제
			visit[i] = true;  // 일단 첫 노드부터 탐색
			dfs(i, 0);
			visit[i] = false;  // 해당 노드에서 시작했을 때 관계를 못 찾은 경우, 다른 노드에서 접근할 수도 있으므로 탐색 후보로 돌림
			if(answer != 0) // 만약 해당 탐색을 통해 정답을 찾은 경우 탐색 종료
				break;  // 여러 관계를 통해 여러 답이 생성될 수 있는데, 먼저 답을 찾은 경우 그 뒤는 굳이 볼 필요가 없음
		}
		System.out.println(answer);
		// 결과적으로 해당 문제는 연결된 곳까지 가보고 답이 안 된다면 직전의 분기까지 되돌아가 답을 찾는 문제
	}

	static void dfs(int s, int cnt) {
		if(cnt == 4) {  // 문제에서 주어진 관계가 형성되어있을 경우
			answer = 1;
			return;  // 종료
		}
		int len = graph[s].size();
		for (int i = 0; i < len; i++) {  // 방문하지 않은 노드와 연결된 노드들을 탐색
			int idx = (int) graph[s].get(i);  // 중복된 작성을 피하기 위해 변수처리
			if (!visit[idx]) {  // 해당 노드를 아직 탐색하지 않았다면
				visit[idx] = true;
				dfs(idx, cnt + 1);
				visit[idx] = false;
			}
		}
	}
}
