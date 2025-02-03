package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2661_좋은수열 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		
		solve();
	}
	
	static boolean isValid(String num) {
		for(int i = 1; i <= num.length() / 2; i++) {
			String back = num.substring(num.length() - i, num.length());
            String front = num.substring(num.length() - i * 2, num.length() - i);
            if(back.equals(front)) {
            	return false;
            }
        }
        return true;
	}
	
	static void search(String num) {
		if(num.length() == n) {
			System.out.println(num);
			System.exit(0);
		}
		
		for(int i = 1; i <= 3; i++) {
			if(isValid(num + i)) {
				search(num + i);
			}
		}
	}
	
	static void solve() {
		search("");
	}
}
