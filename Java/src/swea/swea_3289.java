package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_3289 {
	static int[] parent; // 서로소 집합을 표현하는 1차원 배열
	static int n;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			makeSet();
			sb.append("#").append(tc).append(" ");
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int cmd = Integer.parseInt(st.nextToken());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				if (cmd == 0)
					union(a, b);
				else if (cmd == 1) {
					if (findSet(a) == findSet(b))
						sb.append(1);
					else
						sb.append(0);
				}
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	// 서로소 집합을 표현하는 자료구조 생성 및 초기화
	static void makeSet() {
		parent = new int[n + 1];
		for (int i = 1; i <= n; i++) {
			parent[i] = i;
		}
	}

	// 소속된 서로소집합의 대표 원소를 리턴
	static int findSet(int x) {
		// 기저 조건
		// value와 index가 같은 조건
		if (parent[x] == x)
			return x;
		else
//			return findSet(parent[x]);  // 경로 압축 x
			return parent[x] = findSet(parent[x]);
	}

	// 두 서로소집합을 하나로 합침
	// x의 대표자, y의 대표자를 찾아서 합침
	static void union(int x, int y) {
		int px = findSet(x); // x의 최종 대표자 집합 원소
		int py = findSet(y); // y의 최종 대표자 집합 원소

		// 만약 px == py -> x, y는 같은 서로소 집합에 포함
		// 그렇지 않으면 x, y는 서로 다른 서로소 집합에 포함
		parent[py] = px;
	}
}
