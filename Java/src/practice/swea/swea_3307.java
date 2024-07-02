package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_3307 {
	static int n, T, len;
	static int[] input;
	static int[] lis;  // memo
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		
		for(int t = 1; t <= T; t++) {
			n = Integer.parseInt(br.readLine());
			input = new int[n];
			lis = new int[n];
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i = 0; i < n; i++)
				input[i] = Integer.parseInt(st.nextToken());
			
			// 풀이
			len = 0;
			for(int i = 0; i < n; i++) {
				lis[i] = 1;  // 자기 자신 수로 만들 수 있는 lis가 1이므로 
				// 맨 앞에서 현재 따지는 i보다 작은 수까지 
				for(int j = 0; j < i; j++) {
					// j로 따지는 수가 현재 i번째 수보다 작은 수 
					// j의 lis의 값은 i의 list보다 크거나 같은 경우
					if(input[j] < input[i] && lis[j] >= lis[i])
						lis[i] = lis[j] + 1;
					len = Math.max(len, lis[i]);
				}
			}
			sb.append("#").append(t).append(" ").append(len).append("\n");
		}
		System.out.println(sb);
	}
}
