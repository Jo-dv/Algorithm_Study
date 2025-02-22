package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class BOJ_10597_순열장난 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static String nums;
	static HashSet<Integer> visited = new HashSet<>();
	static StringBuilder sb = new StringBuilder();
	static int n;
	static boolean flag = false;

	public static void main(String[] args) throws IOException {
		nums = br.readLine();
		n = nums.length() <= 9 ? nums.length() : 9 + ((nums.length() - 9) / 2);

		solve();
	}

	static void search(int idx) {
		if (visited.size() == n) {
			System.out.println(sb);
			System.exit(0);;
		}
		if (idx == nums.length()) {
			return;
		}

		int num1 = Integer.parseInt(nums.substring(idx, Math.min(idx + 1, nums.length())));  // 1의 자리
		int num2 = Integer.parseInt(nums.substring(idx, Math.min(idx + 2, nums.length())));  // 10의 자리
		if (0 < num1 && num1 < 10 && !visited.contains(num1)) {
			visited.add(num1);
			sb.append(num1).append(" ");
			search(idx + 1);
			sb.delete(sb.length() - 2, sb.length());  // 현재 마지막 위치 기준, 숫자 및 공백 포함 제거
			visited.remove(num1);
		}

		if (9 < num2 && num2 < 51 && !visited.contains(num2)) {  // num2가 주어진 범위 내의 10의 자리 숫자라면
			visited.add(num2);
			sb.append(num2).append(" ");
			search(idx + 2);
			sb.delete(sb.length() - 3, sb.length());
			visited.remove(num2);
		}
	}

	static void solve() {
		search(0);
	}
}
