package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


// 0001: 1번 도시 방문
// 1010: 2, 4번 도시 방문
// 1101: 1, 3, 4번 도시 방문

// memo[i][j]: 현재 i번 도시가 있고, 거쳐온 도시가 j일 때, 남은 도시를 방문하는 데 필요한 최소 비용
// memo[3][1100101]: 1, 3, 6, 7 도시를 거쳐서 현재 3번 도시일 때, 남은 2, 4, 5를 방문하는 데 드는 최소 비용
// memo[2][1100111] + (3 -> 2)
// memo[4][1100111] + (3 -> 4)
// memo[5][1100111] + (3 -> 5) 
// 중 최소 선택
public class boj_2098_다시풀기 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, allmask, inf = 999_999_999;
	static int[][] w;
	static int[][] memo;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		w = new int[n][n];
		
		allmask = (1 << n) - 1;  // n이 5이면 1 << 5: 100000, 1을 빼면 11111(5자리가 모두 1)
		memo = new int[n][allmask];
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++)
				w[i][j] = Integer.parseInt(st.nextToken());
		}
		
		// 0번째 도시에서 출발
		System.out.println(tsp(0, 1));
	}
	
	static int tsp(int idx, int mask) {
		// 기저 조건
		if(mask == allmask) {  // 모든 도시 방문 완료, 처음(0)으로 되돌아가는 비용만 계산
			if(w[idx][0] == 0)
				return inf;
			else
				return w[idx][0];
		}
		
		// 더 도시를 방문해야 한다.
		if(memo[idx][mask] != 0)
			return memo[idx][mask];
		// 처음
		memo[idx][mask] = inf;
		
		// 방문하지 않는 도시를 방문(재귀)
		for(int i = 0; i < n; i++) {
			if(w[idx][i] == 0 || (mask & 1 << i) != 0)  // 갈 수 없거나, 이미 방문한 경우 skip
				continue;
			memo[idx][mask] = Math.min(memo[idx][mask], tsp(i, mask | 1 << i) + w[idx][i]);
		}
		return memo[idx][mask];
	}

}
