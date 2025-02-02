package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2023_신기한소수 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());

		solve();
	}

	static boolean isPrime(int num) {
		if (num < 2) {
			return false;
		}
		
		for (int i = 2; i * i <= num; i++) {
			if (num % i == 0) {
				return false;
			}
		}
		
		return true;
	}
	
	static void search(int num, int size) {
		if (size == n) {
            sb.append(num).append("\n");
            return;
        }

        for (int i = 1; i <= 9; i++) {
            int next = num * 10 + i;
            if (isPrime(next)) {
                search(next, size + 1);
            }
        }
	}

	static void solve() {
		search(0, 0);
		
		System.out.println(sb);
	}
}
