package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;

// pq 사용 x -> 큐 안에 있는 전체 객체를 heap으로 유지 비용
// 가장 가까운 적과의 거리를 직접 계산
// 거리를 직접 계산하므로 Enemy의 d 멤버는 삭제
// enemyCopy -> 입력을 처리하면서 동적으로 add() -> ArrayList는 합당
// enemy -> 수를 알고있으므로 배열 -> 삭제는 null로 처리
// Enemy class -> 배열로 변경
public class boj_17135_3 {
	
	static int N, M, D, enemySize, max;
	static int[] archer = new int[3];  // 조합으로 선택한 궁수의 x 좌표
	static int[][] enemy;  // 시뮬레이션 과정에서 사용되는 (변하는 Enemy를 관리)
	static List<int[]> enemyCopy = new ArrayList<>();  // 최초 테케입력으로부터 조합 완성 휴 시뮬레이션을 시작할 때마다 사용(원본)
	// 궁수로부터 가장 가까운 적을 찾는 방법
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());  // 행
		M = Integer.parseInt(st.nextToken());  // 열
		D = Integer.parseInt(st.nextToken());  // 사정 거리
		
		// 적군
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < M; j++) {
				int n = Integer.parseInt(st.nextToken());
				if(n == 1) enemyCopy.add(new int[] {i, j, 0});
			}
		}
		enemySize = enemyCopy.size();
		// enemy[] 생성
		enemy = new int[enemySize][3];
		comb(0, 0);  // m개 x자리 (y는 바로 옆)에서 3개를 뽑아서 archer[] (tgt)에 담아두고 처리
		System.out.println(max);
	}
	
	static void check() {
		// 시뮬레이션 진행
		// 적군 초기화
		for (int i = 0; i < enemySize; i++) {
			int[] e = enemyCopy.get(i);
			enemy[i] = new int[] {e[0], e[1], e[2]};  // 복제 -> 새로 생성
		}
		// while() 시뮬레이션 진행
		int dead = 0;
		int enemyCt = enemySize; // enemy[]에 아직 살아있는 적의 수
		while(true) {
			// 궁수 3명이 한 명씩 적군을 쏜다.
			for (int i = 0; i < 3; i++) {
				// 가장 가까운 적
				int ac = archer[i];  // 현재 궁수의 x좌표
				int size = enemySize;  // 현재 적군의 크기

				int minD = Integer.MAX_VALUE;
				int minX = Integer.MAX_VALUE;
				int minIdx = -1;  // 가장 가까운 거리에 있는 적의 index

				for (int j = 0; j < size; j++) {  // 현재 모든 적군에 대해서
					int[] e = enemy[j];
					if(e == null) continue; 
					int d = Math.abs(ac - e[1]) + Math.abs(N - e[0]);
					
					if(d > D)  // 사정거리 밖 적은 무시
						continue;
					
					// 사정거리 안 적이라면
					if(minD == d) {
						if(minX > e[1]) {
							minX = e[1];
							minIdx = j;  // 적읜 index
						}
					}
					else if(minD > d) {
						minD = d;
						minX = e[1];
						minIdx = j;
					}
				}
				
				if(minIdx != -1) {
					enemy[minIdx][2] = 1;
				}
			}
			// 같은 적이 여러 궁수에게 공격당할 수 있다. -> 바로 적에서 삭제 x, 표시만 하고 for문 이후에서 정리

			// 죽은 적군을 제거, 남은 적국은 한 칸 아래로 이동
			for (int i = 0; i < enemySize; i++) {
				if(enemy[i] == null) continue;  // 이미 죽은 것은 제외
				if(enemy[i][2] == 1) {  // 이미 죽은 것은 제외
					enemy[i] = null;
					dead++;
					enemyCt--;
				}
				else if(enemy[i][0] == N - 1) {  // 이미 죽은 것은 제외
					enemy[i] = null;
					enemyCt--;
				}
				else
					enemy[i][0]++;

			}
			// 시뮬레이션 종료 조건
			if(enemyCt == 0) break;
		}
		max = Math.max(max, dead);
	}
	
	static void comb(int srcIdx, int tgtIdx) {
		if(tgtIdx == 3) {
			// simulation
			check();
			return;
		}
		
		if(srcIdx == M) return;
		
		archer[tgtIdx] = srcIdx;  // 궁수 자리 선택
		comb(srcIdx + 1, tgtIdx + 1);
		comb(srcIdx + 1, tgtIdx);
	}
}
