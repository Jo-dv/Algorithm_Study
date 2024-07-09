package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_9328_열쇠 {
	static BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
	static StringTokenizer st;
	static int t;
	static int h, w;
	static char[][] map;
	static String keys;
	static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static boolean[] key_info;
	static boolean[][] visited;
	static int answer;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < t; i++) {
			st = new StringTokenizer(br.readLine());
			h = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			map = new char[h+2][w+2];  // 빌딩의 가장자리를 추가하기 위한 공간 +2
		
			for(int y = 0; y < h+2; y++) {
				Arrays.fill(map[y], '.');
				if(1 <= y && y <= h) {
					String row = br.readLine();
					for(int x = 1; x <= w; x++)
						map[y][x] = row.charAt(x-1);
				}
			}

			keys = br.readLine();
			key_info = key_init();
			visited = new boolean[h+2][w+2];
			answer = 0;
			
			solve();
		}
		
		System.out.println(sb);
	}
	
	static boolean[] key_init() {
		boolean[] result = new boolean[26];  // 열쇠 소유 정보
		
		for(int i = 0; i < keys.length(); i++) {
			if(!keys.equals("0")) {  // 열쇠가 없다는 정보는 필요 없음
				int key = keys.charAt(i) - 'a';  // 아스키 값을 이용해 열쇠 정보 저장
				result[key] = true;
			}
		}
		
		return result;
	}
	
	static boolean is_valid(int y, int x) {
		return 0 <= y && y < h + 2 && 0 <= x && x < w + 2 && !visited[y][x] && map[y][x] != '*';
	}
	
	
	static void search(int y, int x) {
		int my, mx;
		Queue<Node> q = new ArrayDeque<>();
		List<Node>[] doors = new ArrayList[26];  // 열지 못하는 문에 대한 정보를 저장할 리스트
		for(int i = 0; i < 26; i++)
			doors[i] = new ArrayList<>();
		q.offer(new Node(y, x));
		visited[y][x] = true;
		
		while(!q.isEmpty()) {
			Node current = q.poll();
			
			for(int[] d : directions) {
				my = current.y + d[0];
				mx = current.x + d[1];
				
				if(is_valid(my, mx)) {					
					visited[my][mx] = true;
					
					if(map[my][mx] == '$') {
						q.offer(new Node(my, mx));
						answer++;
					}
					else if('a' <= map[my][mx] && map[my][mx] <= 'z') {  // 열쇠 발견
						if (!key_info[map[my][mx] - 'a']) {
                            key_info[map[my][mx] - 'a'] = true;
                            for (Node door : doors[map[my][mx] - 'a'])  // 열 수 있는 문들은 탐색 범위에 포함
                                q.offer(door);
						}
						q.offer(new Node(my, mx));
					}
					else if('A' <= map[my][mx] && map[my][mx] <= 'Z') {  // 문 발견
						if(!key_info[map[my][mx] - 65])  // 열쇠가 없다면
							doors[map[my][mx] - 65].add(new Node(my, mx));  // 추후 현재 탐색이 종료되면 열쇠를 발견할 수 있기 때문
						else
							q.offer(new Node(my, mx));
					}
					else  // 길 발견
						q.offer(new Node(my, mx));
				}
			}
		}
	}

	static void solve() {
		search(0, 0);
		
		sb.append(answer).append("\n");
	}

	static class Node {  // 좌표 정보를 저장할 노드 클래스
		int y, x;

		public Node(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}
}