package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class BOJ_15565_귀여운라이언 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, k;
	static int[] arr;
	static int answer = 1000001;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		
		solve();
	}
	
	static void solve() {
		ArrayDeque<Integer> slider = new ArrayDeque<>();
		
		for(int i = 0; i < n; i++) {  // 값들을 하나씩 확인해서
			if(arr[i] == 1) {
				slider.add(i);
				if(slider.size() == k) {  // k개의 목표값을 찾으면
					answer = Math.min(answer, slider.peekLast() - slider.peekFirst() + 1);  // 시작 위치와 끝 위치에 따른 길이 비교
					slider.pollFirst();  // 다음 조합을 찾기 위해 시작 값 제거
				}
			}
		}
		System.out.println(answer == 1000001 ? -1 : answer);  //  값의 변경이 없는 경우, 즉 k개의 목표값이 없는 경우 -1 출력
	}

}
