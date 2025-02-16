package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_2118_두개의탑 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static int[] tower;
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		tower = new int[n + 1];  // 포인터가 마지막 인덱스까지 탐색할 수 있도록
		
		for(int i = 0; i < n; i++) {
			tower[i] = Integer.parseInt(br.readLine());
		}
		
		solve();
	}
	
	static void solve() {
		int total_distance = Arrays.stream(tower).sum();
		int left = 0, right = 0;
		int forward = tower[right];
		int inverse = 0;

		while(left <= right && right < n) {
			inverse = total_distance - forward;  // 반시계 방향을 따로 관리해 원형 배열을 고려할 필요 없음
			answer = Math.max(answer, Math.min(forward, inverse));

			if(forward == Math.min(forward, inverse)) {  // 시계 방향의 거리가 반시계 방향보다 같거나 작을 때 시계 방향의 거리를 늘림 
				forward += tower[++right];
			} else {
				forward -= tower[left++];  // 시계 방향이 더 크다는 의미이므로 시계 방향의 거리를 줄여 반시계 방향의 거리를 늘림
			}
		}
		
		System.out.println(answer);
	}
}
