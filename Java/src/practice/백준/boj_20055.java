package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_20055 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, k;
	static int[] arr;
	static boolean[] status;
	static int answer;
	
	public static void main(String[] args) throws IOException {
		// 박스는 올리는 위치 -> 1번 위치에서만 올릴 수 있다. 반대로 내리는 위치인 N에 도달하면 즉시 내려진다.
		// 각 컨베이어 칸의 내구도 A를 가진다.
		// 로봇이 올려지거나 이동하면 내구도는 즉시 1이 감소한다. -> 로봇은 벨트 위를 자유롭게 이동할 수 있다.
		// 로봇을 건너편으로 이동시키려 한다. 순서는 다음과 같다
		// 1. 벨트가 각 칸 위 로봇과 함께 한칸 회전
		// 2. 로봇이 올라간 순서대로 회전 방향으로 한 칸 이동 가능 -> 이동불가면 가만히 있음
		// 2.1 이동하려는 곳에 로봇은 없어야 하며, 내구도는 1 이상 남아야 한다.
		// 3. 올리는 위치에 내구도가 남아있으면 로봇을 올린다.
		// 4. 내구도가 0인 칸이 k개 이상이면 종료 그렇지 않으면 1로 이동
		// 종료 시점에서 몇 번째 단계가 진행중이었는지 출력 -> 단순히 어떠한 행동아 진행되었는지
		st = new StringTokenizer(br.readLine()); 
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		arr = new int[n * 2 + 1];
		status = new boolean[n * 2 + 1];
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i <= n * 2; i++) {
			arr[i < n + 1 ? i : 2 * n - (i - (n + 1))] = Integer.parseInt(st.nextToken());
		}
		
		answer = run();
		System.out.println(answer);
	}
	static int run() {
		// 조건이 만족될 때까지 반복
		int break_point = 0;
		int idx = 3;
		int time = 1;
		arr[1]--;
		arr[2]--;
		status[2] = true;
		
		while(break_point < k) {
			for(int i = 1; i < idx; i++) {
				if(arr[i] == 0) {
					break_point++;
					status[i] = true;
				}
			}
			for(int i = idx; i > 0; i--) {  // 두 번째부터
				if(!status[i]) {
					if(arr[i - 1] != 0) {
						status[i - 1] = false;
						arr[i]--;
						time++;
					}
					status[i] = true;
				}
				if(status[1])
					break;
			}
			if(arr[idx] == 0) {
				break_point++;
				status[idx] = true;
			}
			idx = (idx + 1) % ((n * 2) + 1);
		}
		return time;
	}
}
