package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 18개 카드 중에 규영이의 카드 9개 고정 나머지 9개 카드를 어떤 순서대로 구성하느냐에 따라 규영이의 카드와 승부가 달라지는 분
// 인영이의 카드 9개를 순열로 처리 - 모든 경우에 대해 규영이카드와 게임을 진행 win, lose 누적
public class swea_6808_2 {

	static int T, win, lose, N = 9;
	static int[] input = new int[19];
	static int[] guCard = new int[9];
	static int[] inCard = new int[9]; // src
	static int[] tgt = new int[9];
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {
			// 초기화
			win = 0;
			lose = 0;
			Arrays.fill(input, 0);

			// 입력
			StringTokenizer st = new StringTokenizer(br.readLine());

			// 규영이 카드
			int num = 0;
			for (int i = 0; i < N; i++) {
				num = Integer.parseInt(st.nextToken());
				input[num] = 1;
				guCard[i] = num;
			}

			// 인영이 카드
			num = 0;
			for (int i = 1; i <= 18; i++) {
				if (input[i] == 0) {
					inCard[num++] = i;
				}
				;
			}

			// 풀이
			perm(0);

			sb.append("#").append(" ").append(t).append(" ").append(win).append(" ").append(lose).append("\n");
		}
		System.out.println(sb);
	}

	static void perm(int srcidx) {
		if (srcidx == N) {
			check();
			return;
		}

		// i가 srcidx부터 -> 자기 자신 포함
		for (int i = srcidx; i < inCard.length; i++) {
			// i와 srcidx를 교환
			int temp = inCard[srcidx];
			inCard[srcidx] = inCard[i];
			inCard[i] = temp;

			perm(srcidx + 1);
			// i와 srcidx 원본
			temp = inCard[srcidx];
			inCard[srcidx] = inCard[i];
			inCard[i] = temp;
		}
	}

	static void check() {
		int guSum = 0;
		int inSum = 0;

		for (int i = 0; i < N; i++) {
			if (guCard[i] > tgt[i])
				guSum += guCard[i] + tgt[i];
			else
				inSum += inCard[i] + tgt[i];
		}

		if (guSum > inSum)
			win++;
		else if (guSum < inSum)
			lose++;
	}
}