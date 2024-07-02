package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 검증할 유효성
// 이진 트리의 아래부터 검증 수행
// 1. 검증하는 노드가 숫자일 때 자식은 없는지 확인
// 2. 검증하는 노드가 연산자면 자신의 유효성에 의존하여 구성을 어떻게 할지 확인
public class swea_1233_3 {
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

			ans = 1;
			int idx = n;
			while(idx != 1) {
				if(!Character.isDigit(node[idx]) || !Character.isDigit(node[idx-1]) || Character.isDigit(node[idx/2])) {
					ans = 0;
					break;
				}
				node[idx / 2] = '1';
				idx -= 2;
			}
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		}
		System.out.println(sb);
	}
}
