package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1074 {
	static int n, r, c;
	static int y, x;
	static int answer = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		int size = (int) Math.pow(2, n);
		search(r, c, size);  // 시작 좌표를 0, 0부터 탐색하면 해당 좌표가 있는 영역을 탐색하기 위해 쓸데없는 시간이 소요
		System.out.println(answer);
	}
	
	static void search(int y, int x, int s) {  // 주어진 좌표내에서 재귀적으로 쪼개짐, 범위를 설정하지 않고 다 탐색하면 마찬가지로 쓸데없는 시간이 소요
		if(s == 1)
			return;
		int half_s = s / 2;  // 탐색할 때마다 탐색 범위를 반씩 줄임
		if(y < half_s && x < half_s)  // 4분면 중 좌측 상단 -> (0, 0) ~ (n/2, n/2)
			search(y, x, half_s);
		else if(y < half_s && x < x + half_s) {  // 4분면 중 우측 상단 -> (0, n/2) ~ (n/2, n)
			answer += half_s * half_s * 1;
			search(y, x - half_s, half_s);
		}
		else if(y < y + half_s && x < half_s) {  // 4분면 중 좌측 하단 -> (n/2, 0) ~ (n, n/2)
			answer += half_s * half_s * 2;
			search(y - half_s, x, half_s);
		}
		else {  // 4분면 중 좌측 하단 -> (n/2, n/2) ~ (n, n)
			answer += half_s * half_s * 3;  // 가장 마지막에 탐색되는 영역으로 동일한 연산이 세 번 반복됨 -> 다른 4분면들을 모두 방문해야 함
			search(y - half_s, x - half_s, half_s);
		}
		// 탐색의 범위를 줄여가는 것이기 때문에 주어진 좌표에서 일정 범위만큼 빼줘야 함, 또한 조건문의 순서는 탐색 순서에 해당
	}

}
