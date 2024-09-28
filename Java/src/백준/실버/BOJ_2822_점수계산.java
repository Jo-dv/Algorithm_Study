package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map.Entry;
import java.util.Arrays;
import java.util.TreeMap;

public class BOJ_2822_점수계산 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static TreeMap<Integer, Integer> scores = new TreeMap<>();
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		for(int i = 1; i <= 8; i++)
			scores.put(Integer.parseInt(br.readLine()), i);

		solve();
	}
	
	static void solve() {
		int[] idx = new int[5];
		int total_score = 0;
				
		for(int i = 0; i < 5; i++) {
			Entry<Integer, Integer> temp = scores.pollLastEntry();
			total_score += temp.getKey();
			idx[i] = temp.getValue();
		}
		Arrays.sort(idx);

		System.out.println(total_score);
		for(int i: idx)
			System.out.print(i + " ");
	}
}
