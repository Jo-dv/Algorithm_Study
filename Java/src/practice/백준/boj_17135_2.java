package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

// pq 사용 x -> 큐 안에 있는 전체 객체를 heap으로 유지 비용
// 가장 가까운 적과의 거리를 직접 계산
// 거리를 직접 계산하므로 Enemy의 d 멤버는 삭제
public class boj_17135_2 {
	
	static int N, M, D, max;
	static int[] archer = new int[3];  // 조합으로 선택한 궁수의 x 좌표
	static List<Enemy> enemy = new ArrayList<>();  // 시뮬레이션 과정에서 사용되는 (변하는 Enemy를 관리)
	static List<Enemy> enemyCopy = new ArrayList<>();  // 최초 테케입력으로부터 조합 완성 휴 시뮬레이션을 시작할 때마다 사용(원본)
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
				if(n == 1) enemyCopy.add(new Enemy(i, j));
			}
		}
		
		comb(0, 0);  // m개 x자리 (y는 바로 옆)에서 3개를 뽑아서 archer[] (tgt)에 담아두고 처리
		System.out.println(max);
	}
	
	static void check() {
		// 시뮬레이션 진행
		// 적군 초기화
		enemy.clear();
		for (Enemy e : enemyCopy) {
			enemy.add(new Enemy(e.y, e.x));  // 객체를 공유하지 않고, 내용만 복사해서 새로운 객체 생성
		}
		// while() 시뮬레이션 진행
		int dead = 0;
		while(true) {
			// 궁수 3명이 한 명씩 적군을 쏜다.
			for (int i = 0; i < 3; i++) {
				// 가장 가까운 적
				int ac = archer[i];  // 현재 궁수의 x좌표
				int size = enemy.size();  // 현재 적군의 크기

				int minD = Integer.MAX_VALUE;
				int minX = Integer.MAX_VALUE;
				int minIdx = -1;  // 가장 가까운 거리에 있는 적의 index

				for (int j = 0; j < size; j++) {  // 현재 모든 적군에 대해서
					Enemy e = enemy.get(j);
					int d = Math.abs(ac - e.x) + Math.abs(N - e.y);
					
					if(d > D)  // 사정거리 밖 적은 무시
						continue;
					
					// 사정거리 안 적이라면
					if(minD == d) {
						if(minX > e.x) {
							minX = e.x;
							minIdx = j;  // 적읜 index
						}
					}
					else if(minD  > d) {
						minD = d;
						minX = e.x;
						minIdx = j;
					}
				}
				if(minIdx != -1) {
					enemy.get(minIdx).dead = true;
				}
			}
			// 같은 적이 여러 궁수에게 공격당할 수 있다. -> 바로 적에서 삭제 x, 표시만 하고 for문 이후에서 정리

			// 죽은 적군을 제거, 남은 적국은 한 칸 아래로 이동
			for (int i = enemy.size() - 1; i >= 0; i--) {
				Enemy e = enemy.get(i);
				if(e.dead) {
					enemy.remove(i);
					dead++;
				}
				else if(e.y == N - 1) {
					enemy.remove(i);
				}
				else {
					e.y++;
				}
			}
			// 시뮬레이션 종료 조건
			if(enemy.size() == 0) break;
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
	
	static class Enemy {
		int y, x;  // d: 궁수와의 거리
		boolean dead;  // 사망 여부
		
		Enemy(int y, int x) {  // d, dead -> 시물레이션을 진행하면서 setting
			this.y = y;
			this.x = x;
		}
	}

}
