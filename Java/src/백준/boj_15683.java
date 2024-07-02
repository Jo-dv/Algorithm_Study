package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class boj_15683 {
	static int n, m;
	static int[][] maps;
	static int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};  // 방향 벡터
	static int answer = Integer.MAX_VALUE;
	static List<int[]> cctv;  // cctv의 위치를 담을 리스트
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		maps = new int[n][m];
		cctv = new ArrayList<>();
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++) {
				maps[i][j] = Integer.parseInt(st.nextToken());
				if(0 < maps[i][j] && maps[i][j] < 6)  // 맵을 초기화 하면서 cctv의 위치를 리스트에 저장
					cctv.add(new int[] {i, j});
			}
		}
		rotate(0);  // 첫 cctv부터 탐색 시작
		System.out.println(answer);
	}
	
	static void rotate(int idx) {
		if(idx == cctv.size()) {  // 모든 cctv에 대해 탐색이 끝났다면
			int check = 0;
			for(int i = 0; i < n; i++)
				for(int j = 0; j < m; j++)
					if(maps[i][j] == 0) check++;  // 처리되지 않은 공간 카운팅
			answer = check < answer ? check : answer;  // 최소값으로 갱신
			return;
		}
		
		int y = cctv.get(idx)[0];  // 현재 cctv 위치
		int x = cctv.get(idx)[1];
		int[][] origin = new int[n][m];  // 탐색으로 인해 변형된 맵을 되돌리기 위한 원본 맵, 각 cctv의 조합에 따라 결과가 달라지므로 cctv를 조작 후 원래대로 돌려줘야 함
		
		for(int rotate_num = 0; rotate_num < 4; rotate_num++) {  // cctv는 상하좌우 네 방향에 대해 90도로 돌아가므로
			for(int i = 0; i < n; i++)
				origin[i] = maps[i].clone();  // 2차원 배열은 한 줄씩 카피해야 함
			
			if(maps[y][x] == 1)   // cctv에 맞춰 탐색
				search(y, x, rotate_num);  // 기본 우측을 가리키며 시계 방향으로 벡터가 세팅, 벡터의 순서는 취향껏 설정 가능
			else if(maps[y][x] == 2) {
				search(y, x, rotate_num);
				search(y, x, rotate_num + 2);
			}
			else if(maps[y][x] == 3) {
				search(y, x, rotate_num);
				search(y, x, rotate_num + 3);
			}
			else if(maps[y][x] == 4) {
				search(y, x, rotate_num);
				search(y, x, rotate_num + 2);
				search(y, x, rotate_num + 3);
			}
			else if(maps[y][x] == 5) {
				search(y, x, rotate_num);
				search(y, x, rotate_num + 1);
				search(y, x, rotate_num + 2);
				search(y, x, rotate_num + 3);
			}
			
			rotate(idx + 1);  // 다음 cctv로
			
			for(int i = 0; i < n; i++)  // 조작된 맵을 원상복구
				maps[i] = origin[i].clone();
		}
	}
	
	static void search(int y, int x, int foward) {  // cctv가 탐지할 수 있는 영역을 처리
		int my = y + direction[foward % 4][0];  // 모듈러 연산을 통해 회전 횟수 증가에 따른 인덱싱 아웃을 방지
		int mx = x + direction[foward % 4][1];
		while((0 <= my && my < n && 0 <= mx && mx < m) && maps[my][mx] != 6) {  // 탐색할 위치가 유효 범위이며 벽이 아닌 경우
			if(maps[my][mx] == 0)  // 빈 칸에 대해서만, 그렇지 않으면 겹치는 방향의 cctv도 지워짐 -> 조합이 망가짐
				maps[my][mx] = -1;
			y = my;  // 현재 위치 갱신
			x = mx;
			my = y + direction[foward % 4][0];  // 현재 위치를 바탕으로 탐색할 위치 생성
			mx = x + direction[foward % 4][1];
		}
		return;
	}
}
