package practice.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Comparator;
import java.util.Deque;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class swea_5658 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int t;
	static int n, k;
	static String num;
	static Deque<Character> q;
	static Set<Integer> set;
	
	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc <= t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			num = br.readLine();
			q = new ArrayDeque<Character>();
			set = new TreeSet<>(Comparator.reverseOrder());
			for(int i = 0; i < n; i++)
				q.add(num.charAt(i));  // 문자열을 회전하기 위해 문자열과 큐를 따로 둠
			String data = "";
			
			for(int i = 0; i < n/4; i++) {  // n/4 + 1만큼 회전하면 원점
				for(int j = 0; j < n; j++) {
					data += num.charAt(j);
					if(data.length() == n/4) {  // 현재 값을 각 변의 길이가 될 때마다 저장
						set.add(Integer.parseInt(data, 16));
						data = "";  // 다음 값을 받기 위해 초기화
					}
				}
				q.addFirst(q.pollLast());  // 현재 상태에서의 값이 다 들어오면 큐 회전
				num = "";  // 새로운 큐 생성
				for (Character j : q)  // 회전된 큐를 문자열로 변환
					num += j;
			}
			sb.append("#").append(tc).append(" ").append(set.toArray()[k-1]).append("\n");
		}
		System.out.println(sb);
	}

}
