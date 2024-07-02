package 백준;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_2252 {
	
	static int n, m;
	static int[] topo;  // 차수
	static List<List<Integer>> g = new ArrayList<>();
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());  // 학생 수
		m = Integer.parseInt(st.nextToken());  // 비교 횟수
		topo = new int[n + 1];  // 0 is dummy
		
		//adl
		for(int i = 0; i <= n; i++) {
			g.add(new ArrayList<Integer>());
		}
		
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			// a -> b
			g.get(a).add(b);
			topo[b]++;  // 진입 차수 증가
		}
		
		// 풀이
		Queue<Integer> q = new ArrayDeque<Integer>();
		
		// 진입차수가 0인 번호를 큐에 저장
		for(int i = 1; i <= n; i++) {
			if(topo[i] == 0) {
				q.offer(i);
			}
		}
		
		// 큐를 이용해서 꺼내면서 연결을 끊고 다시 진입차수가 0인 학생을 큐에 담는다.
		while(!q.isEmpty()) {
			int no = q.poll();
			
			// 큐에서 꺼낸 번호가 바로 줄세우기 번호
			sb.append(no).append(" ");
			
			// no 학생으로부터 다른 학생을 모두 대상으로 
			List<Integer> list = g.get(no);
			int size = list.size();
			for(int i = 0; i < size; i++) {
				int temp = list.get(i);
				topo[temp]--;  // no -> temp 관계인데 no를 그래프에서 재거하므로 temp의 진입차수가 1 감소
				if(topo[temp] == 0)
					q.offer(temp);
			}
		}
		System.out.println(sb);
	}

}
