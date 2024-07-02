package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_15649 {
	static int n = 0;
	static int m = 0;
	static int[] res;
	static boolean[] check;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		sb = new StringBuilder();
		
		res = new int[m];
		check = new boolean[n];

		perm(0);
		System.out.println(sb);
	}
	
	static void perm(int idx) {
		if(idx == m) {
			for (int i : res)
				sb.append(i).append(" ");
			sb.append("\n");
			return;
		}
		for(int i = 0; i < n; i++) {
			if(check[i])
				continue;
			res[idx] = i + 1;
			check[i] = true;
			perm(idx + 1);
			check[i] = false;
		}
	}
}
