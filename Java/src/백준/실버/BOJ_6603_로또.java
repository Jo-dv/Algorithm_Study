package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_6603_로또 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static List<Integer> test_case;
	static int k;
	static Object[] s;
	static List<Integer> answer;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		while(true) {
			test_case = new ArrayList<>();
			st = new StringTokenizer(br.readLine());
			
			while(st.hasMoreTokens())
				test_case.add(Integer.parseInt(st.nextToken()));
			k = test_case.get(0);
			if(k == 0)
				break;
			
			s = test_case.subList(1, k + 1).toArray();
			answer = new ArrayList<>();
			search(0, 0);
			sb.append("\n");
		}
		System.out.println(sb);
	}
	
	static void search(int idx, int cnt) {
		if(idx == k) {
			if(cnt == 6) {
				for(int num: answer)
					sb.append(num).append(" ");
				sb.append("\n");
			}
			return;
		}
		
		answer.add((Integer) s[idx]);
		search(idx + 1, cnt + 1);  // 현재 값 선택하고, 선택된 수 갱신
		answer.remove(answer.size() - 1);
		search(idx + 1, cnt);
	}
}
