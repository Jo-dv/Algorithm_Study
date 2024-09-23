package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_1043_거짓말 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static List<Integer> true_people;
	static List<Integer>[] participants;
	static int[] parents;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		
		st = new StringTokenizer(br.readLine());
		int people = Integer.parseInt(st.nextToken());
		true_people = new ArrayList<Integer>();
		for(int i = 0; i < people; i++)
			true_people.add(Integer.parseInt(st.nextToken()));
		
		participants = new ArrayList[m + 1];
		for(int i = 0; i <= m; i++)
			participants[i] = new ArrayList<>();
		
		for(int i = 1; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			int participant = Integer.parseInt(st.nextToken());
			for(int j = 0; j < participant; j++)
				participants[i].add(Integer.parseInt(st.nextToken()));
		}
		
		solve();
	}
	
	static int[] init_parents() {
		int[] parents = new int[n + 1];
		for(int i = 1; i <= n; i++)
			parents[i] = i;
		
		return parents;
	}
	
	static int find(int x) {
		if(parents[x] == x)
			return x;
		return parents[x] = find(parents[x]);
	}
	
	static void union(int x, int y) {
		x = find(x);
		y = find(y);
		
		if(true_people.contains(x))  // x가 진실을 아는 사람이라면
			parents[y] = x;
		else if(true_people.contains(y))  // y가 진실을 아는 사람이라면
			parents[x] = y;
		else
			parents[y] = x;  // 일반 연결

			
	}
	
	static void solve() {
		parents = init_parents();
		
		int len = 0;
		if (!true_people.isEmpty()) {  // 진실을 아는 사람들이 있다면
			len = true_people.size();
            for (int i = 1; i < len; i++)
                union(true_people.get(0), true_people.get(i));  // 진실을 아는 사람들끼리 연결
		}

		for(int i = 1; i <= m; i++) { // 파티 참여자들끼리 연결
			len = participants[i].size();
			for(int j = 0; j < len - 1; j++)
				union(participants[i].get(j), participants[i].get(j + 1));
		}

		int answer = 0;
        for (int i = 1; i <= m; i++) {
            boolean lie = true;
            for (int person : participants[i])  // 각 파티의 참여자들에 대해
                if (true_people.contains(find(person))) {  // 참여자들이 진실을 아는 사람들과 연결되어 있는지 확인
                    lie = false;  // 진실을 아는 사람과 연결되어 있다면 거짓말을 할 수 없으므로
                    break;  // 탐색 종료
                }
            if (lie)
                answer++;
        }

        System.out.println(answer);
	}
}