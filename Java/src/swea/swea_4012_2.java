package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// check() 별도의 배열을 따로  n / 2 길이만큼
public class swea_4012_2 {
	static int t, n, size, min;
	static int[][] s;
	static boolean[] select; // 재료 선택 및 비선택
	static int[] arrA, arrB; // 선택된 재로 A, 비선택된 재료 B
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc < t + 1; tc++) {
			n = Integer.parseInt(br.readLine());
			size = n / 2;
			s = new int[n][n];
			select = new boolean[n];
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++)
					s[i][j] = Integer.parseInt(st.nextToken());
			}
			arrA = new int[size];
			arrB = new int[size];
			min = Integer.MAX_VALUE;
			comb(0, 0);
			sb.append("#").append(tc).append(" ").append(min).append("\n");
		}
		System.out.println(sb);
	}

	static void comb(int srcIdx, int tgtIdx) {
		// n / 2개를 선택
		if (tgtIdx == size) {
			check();
			return;
		}

		if (srcIdx == n)
			return;
		select[srcIdx] = true;
		comb(srcIdx + 1, tgtIdx + 1); // 현재 src 중에 tgt 선택
		select[srcIdx] = false;
		comb(srcIdx + 1, tgtIdx);
	}

	// select 배열에서 선택, 비선택 -> 두 그룹으로 나누어서 생각
	// 각각의 그룹별 sum 계산 후 차이 계산 후 min
	static void check() {
		int sumA = 0; // 선택
		int sumB = 0; // 비선택

		int idxA = 0;
		int idxB = 0;
		// seelect[] -> arrA, arrB
		// i, j로 모든 2개씩 조합 전체
		for (int i = 0; i < n; i++) {
			if (select[i])
				arrA[idxA++] = i;
			else
				arrB[idxB++] = i;
		}

		// 2개로 나뉜 각 재료 배열에서 서로 모두 만나게 for - for
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				if (i == j) // 선택된 그룹
					continue;
				sumA += s[arrA[i]][arrA[j]];
				sumB += s[arrB[i]][arrB[j]];
			}
		}
		min = Math.min(min, Math.abs(sumA - sumB));
	}
}
