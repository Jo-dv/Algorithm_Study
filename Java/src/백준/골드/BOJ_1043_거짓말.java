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
		
		if(true_people.contains(x))
			parents[y] = x;
		else if(true_people.contains(y))
			parents[x] = y;
		else
			parents[y] = x;

			
	}
	
	static void solve() {
		parents = init_parents();
		
		int len = 0;
		if (!true_people.isEmpty()) {
			len = true_people.size();
            for (int i = 1; i < len; i++)
                union(true_people.get(0), true_people.get(i));
		}

		for(int i = 1; i <= m; i++) {
			len = participants[i].size();
			for(int j = 0; j < len - 1; j++)
				union(participants[i].get(j), participants[i].get(j + 1));
		}
		
		int answer = 0;
        for (int i = 1; i <= m; i++) {
            boolean canLie = true;
            for (int person : participants[i])
                if (true_people.contains(find(person))) {
                    canLie = false;
                    break;
                }
            if (canLie)
                answer++;
        }

        System.out.println(answer);
	}
}
