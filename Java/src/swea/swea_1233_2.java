package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 검증할 유효성
// 이진 트리의 아래부터 검증 수행
// 1. 검증하는 노드가 숫자일 때 자식은 없는지 확인
// 2. 검증하는 노드가 연산자면 자신의 유효성에 의존하여 구성을 어떻게 할지 확인
public class swea_1233_2 {
	static int n, ans;
	static char[] node;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int t = 1; t < 11; t++) {
			n = Integer.parseInt(br.readLine());
			node = new char[n + 1];

			// 두 번째만
			for (int i = 1; i <= n; i++) {
				node[i] = br.readLine().split(" ")[1].charAt(0);
			}

			// 완전 이진트리지만, 자식이 한쪽만 있는 경우
			if (n % 2 == 0) {
				sb.append("#").append(t).append(" ").append(0).append("\n");
				continue;
			}

			ans = dfs(1) ? 1 : 0; // 바닥에서부터 dfs(1)이 수행되고 최종 결과에 따라 처리
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		}
		System.out.println(sb);
	}

	// x 위치의 노드가 유효한지 검사하고 return
	static boolean dfs(int x) {
		// 기저 조건
		if (x > n)
			return false;

		// 숫자노드인지 아닌지. 만약 숫자면 자식이 없어야 함
		if (Character.isDigit(node[x])) {
			if (x * 2 > n)
				return true;
			return false;
		} else { // 숫자노드가 아니면 연산자이므로 두 자식의 유효성에 의존(둘 다 true면 true 반환)
			return dfs(x * 2) && dfs(x * 2 + 1);
		}
	}
}
