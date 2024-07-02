package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_2798 {
	static int n;
	static int m;
	static int[] cards;
	static int[] selected;
	static int answer = 0;
	static int temp = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		cards = new int[n];
		selected = new int[3];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++)
			cards[i] = Integer.parseInt(st.nextToken());
		solve(0, 0);
		System.out.println(answer);

	}
	
	static void solve(int idx, int target) {
		if(target == 3) {
			temp = selected[0] + selected[1] + selected[2];
			answer = (answer < temp && temp <= m) ? temp : answer;
			temp = 0;
			return;
		}
		if(idx == n)
			return;
		selected[target] = cards[idx];
		solve(idx + 1, target + 1);
		solve(idx + 1, target);
	}
}
