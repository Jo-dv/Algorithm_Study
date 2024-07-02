package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 조합 + 시뮬레이션
public class boj_17135 {
	
	static int n, m, d, max;
	static int[] archer = new int[3];  // 조합으로 선택한 궁수의 x 좌표
	static List<Enemy> enemy = new ArrayList<>();  // 시뮬레이션 과정에서 사용되는 (변하는 Enemy를 관리)
	static List<Enemy> enemyCopy = new ArrayList<>();  // 최초 테케입력으로부터 조합 완성 휴 시뮬레이션을 시작할 때마다 사용(원본)
	// 궁수로부터 가장 가까운 적을 찾는 방법
	static PriorityQueue<Enemy> pq = new PriorityQueue<>((e1, e2) -> e1.d == e2.d ? e1.x - e2.x : e1.d - e2.d);
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());  // 행
		m = Integer.parseInt(st.nextToken());  // 열
		d = Integer.parseInt(st.nextToken());  // 사정 거리
		
		// 적군
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j <m; j++) {
				int n = Integer.parseInt(st.nextToken());
				if(n == 1) enemyCopy.add(new Enemy(j, j));
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
				// 가장 가까운 적 -> 우선순위큐 사용
				pq.clear();
				
				int ac = archer[i];  // 현재 궁수의 x좌표
				int size = enemy.size();  // 현재 적군의 크기
				for (int j = 0; j < size; j++) {  // 현재 모든 적군에 대해서
					Enemy e = enemy.get(j);
					e.d = Math.abs(ac - e.x) + Math.abs(n - e.y);
					if(e.d <= d)  // 사정거리 안에 들어오는 적이면 pq에 담는다
						pq.offer(e);
				}
			}
			// pq를 이용해서 우선순위가 높은 적군을 꺼낸다.
			// 같은 적이 여러 궁수에게 공격당할 수 있다. -> 바로 적에서 삭제 x, 표시만 하고 for문 이후에서 정리
			if(!pq.isEmpty()) {
				pq.poll().dead = true;
			}
			// 죽은 적군을 제거, 남은 적국은 한 칸 아래로 이동
			for (int i = enemy.size() - 1; i >= 0; i--) {
				Enemy e = enemy.get(i);
				if(e.dead) {
					enemy.remove(i);
					dead++;
				}
				else if(e.y == n - 1) {
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
		
		if(srcIdx == m) return;
		
		archer[tgtIdx] = srcIdx;  // 궁수 자리 선택
		comb(srcIdx + 1, tgtIdx);
	}
	
	static class Enemy {
		int y, x, d;  // d: 궁수와의 거리
		boolean dead;  // 사망 여부
		
		Enemy(int y, int x) {  // d, dead -> 시물레이션을 진행하면서 setting
			this.y = y;
			this.x = x;
		}
	}

}
