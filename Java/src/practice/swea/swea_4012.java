package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class swea_4012 {
	static int t, n, size, min;
	static int[][] s;
	static boolean[] select;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		t = Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc < t + 1; tc++) {
			n = Integer.parseInt(br.readLine());
			size = n / 2;
			s = new int[n][n];
			select = new boolean[n];
			for(int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j < n; j++)
					s[i][j] = Integer.parseInt(st.nextToken());
			}
			
			min = Integer.MAX_VALUE;
			comb(0, 0);
			sb.append("#").append(tc).append(" ").append(min).append("\n");
		}
		System.out.println(sb);
	}
	
	static void comb(int srcIdx, int tgtIdx) {
		// n / 2개를 선택
		if(tgtIdx == size) {
			check();
			return;
		}
		
		if(srcIdx == n)
			return;
		select[srcIdx] = true;
		comb(srcIdx + 1, tgtIdx + 1);  // 현재 src 중에 tgt 선택
		select[srcIdx] = false;
		comb(srcIdx + 1, tgtIdx);
	}
	
	// select 배열에서 선택, 비선택 -> 두 그룹으로 나누어서 생각
	// 각각의 그룹별 sum 계산 후 차이 계산 후 min
	static void check() {
		int sumA = 0;  // 선택
		int sumB = 0;  // 비선택
		
		// i, j로 모든 2개씩 조합 전체
		for (int i = 0; i < n - 1; i++) {
			for (int j = i + 1; j < n; j++) {
				if(select[i] && select[j]) {  // 선택된 그룹
					sumA += s[i][j];
					sumA += s[j][i];
				}
				else if(!select[i] && !select[j]) {  // 선택되지 않은 그룹
					sumB += s[i][j];
					sumB += s[j][i];
				}
			}
		}
		min = Math.min(min, Math.abs(sumA - sumB));
	}
}
