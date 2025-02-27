package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class BOJ_2877_4와7 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int k;
	static String answer = "";
	
	public static void main(String[] args) throws IOException {
		k = Integer.parseInt(br.readLine()) + 1;

		solve();
	}

	static void solve() {
		ArrayDeque<Integer> num = new ArrayDeque<>();
		while(k > 0) {
			num.addFirst(k % 2);
			k /= 2;
		}
		
		num.pollFirst();  // 더미값
		while(!num.isEmpty()) {
			if(num.pollFirst() == 0) {
				answer += "4";
			} else {
				answer += "7";
			}
		}
		
		System.out.println(answer);
	}
}
