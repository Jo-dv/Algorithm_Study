package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class boj_15686 {
	
	// 맨해튼 거리
	// 치킨 거리 = 거리들의 총합
	// r, c = (1, 1)
	// 0: 빈 칸, 1: 집, 2: 치킨집
	// 치킨 거리 최소로 만들기
	static int n, m, min, houseSize, srcSize;
	static List<int[]> house, src, tgt;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		house = new ArrayList<int[]>();
		src = new ArrayList<int[]>();  // 치킨집
		tgt = new ArrayList<int[]>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		// 2차원 배열 입력을 받으면서 집, 치킨집에 대해 자료구조를 정리
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++) {
				int num = Integer.parseInt(st.nextToken());
				if(num == 1) house.add(new int[] {i, j}); // 집
				else if(num == 2) src.add(new int[] {i, j});  // 칰킨집 전체
			}
		}
		
		// 풀이
		min = Integer.MAX_VALUE;
		houseSize = house.size();
		srcSize = src.size();
		
		comb(0, 0);
		System.out.println(min);
	}
	
	static void comb(int srcIdx, int tgtIdx) {
		if(tgtIdx == m) {
			// 치킨집 m개를 조합으로 뽑은 상태
			// 이 조합의 치킨거리의 합을 구하고 최소값이면 갱신
			// 모든 집 각각에 대해서 뽑힌 M개의 치킨집 거레 중 최소인 것을 찾아 합을 계산
			int sum = 0;
			for(int i = 0; i < houseSize; i++) {
				int dist = Integer.MAX_VALUE;
				int[] h = house.get(i);  // 각 집에 대한 좌표를 꺼내서
				
				for(int j = 0; j < m; j++) {  // 각 치킨집에 대한 좌표와 맨해튼 거리 계산
					int[] c = tgt.get(j);
					dist = Math.min(dist, Math.abs(h[0] - c[0]) + Math.abs(h[1] - c[1]));
				}
				sum += dist;  // 치킨 거리 계산
			}
			min = Math.min(min, sum);  // 가장 작은 치킨 거리 계산
			return;
		}
		
		if(srcIdx == srcSize)
			return;
		tgt.add(src.get(srcIdx));  // 선택
		comb(srcIdx + 1, tgtIdx + 1);  // 선택 o
		tgt.remove(src.get(srcIdx));  // 선택 x -> 배열은 자연스럽게 다음 index를 덮어쓰는 구조지만 List는 아니기 때문에 원복 필요ㄴ
		comb(srcIdx + 1, tgtIdx);  
		
	}
}
