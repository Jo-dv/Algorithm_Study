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
			
			while(st.hasMoreTokens())  // 다음 토큰이 있을 때까지
				test_case.add(Integer.parseInt(st.nextToken()));
			k = test_case.get(0);
			if(k == 0)
				break;
			
			s = test_case.subList(1, k + 1).toArray();  // 배열 접근과 마찬가지이므로 끝에 k가 아닌 k - 1이 되어야 함
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
		search(idx + 1, cnt + 1);  // 현재 값을 선택했으니 선택된 수의 개수를 갱신하고, 다음 실행에서는 다음 값을 선택해야
		answer.remove(answer.size() - 1);
		search(idx + 1, cnt);  // 현재 수 선택 안 함
	}
}
