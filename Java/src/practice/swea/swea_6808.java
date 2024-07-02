package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_6808 {
	static boolean[] deck;
	static int[] A = new int[9];
	static int card, answer;
	static int facto = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2;   
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		StringTokenizer st;
		int tc = Integer.parseInt(br.readLine());
		
		for(int t = 1; t < tc + 1; t++) {
			deck = new boolean[19];
			answer = 0;
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i < 9; i++) {
				card = Integer.parseInt(st.nextToken());
				deck[card] = true;
				A[i] = card;
			}
			perm(0, 0, 0);
			sb.append("#").append(t).append(" ").append(answer).append(" ").append(facto - answer).append("\n");
		}
		System.out.println(sb);
	}
	
	static void perm(int idx, int A_score, int B_score) {
		if(idx == 9) {
			answer = A_score > B_score ? answer + 1 : answer;
			return;
		}
		
		for(int card = 1; card < 19; card++) {
			if(!deck[card]) {
				deck[card] = true;
				int current_score = A[idx] + card;
				if(A[idx] > card)
					perm(idx + 1, A_score + current_score, B_score);
				else
					perm(idx + 1, A_score, B_score + current_score);
				deck[card] = false;
			}
		}
	}
}
