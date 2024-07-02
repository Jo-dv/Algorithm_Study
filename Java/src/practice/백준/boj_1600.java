package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

// bfs
// k -> 몇 번 사용했는지, visit 추가관리
public class boj_1600 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int k;
	static int w, h;
	static int[][] map;
	static boolean[][][] visit;
	static int answer;
	static int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static int[][] h_direction = {{-2, 1}, {-2, -1}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {1, 2}, {1, -2}};
	static Queue<Node> q = new ArrayDeque<>();
	
	
	public static void main(String[] args) throws IOException {
		k = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		w = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		map = new int[h][w];
		visit = new boolean[h][w][k + 1];
		for(int i = 0; i < h; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < w; j++)
				map[i][j] = Integer.parseInt(st.nextToken());
		}
		answer = 0;
		
		bfs();
	}
	
	static void bfs() {
		// 시작 좌표 처리
		visit[0][0][k] = true;
		q.offer(new Node(0, 0, k, 0));
		// 큐가 빌 때까지 bfs 탐색
		// 한 점에서 다른 이동을 고려할 때
		// #1. 사방 탐색을 갈 수 있는 곳을 찾아서 큐에 담는다.
		// #2. 말처럼 갈 수 있는 곳을 찾아서 큐에 담는다 -> 아직 k만큼 쓰지 않았을 경우 말처럼 갔을 때 k 감소 처리
		// 큐에서 꺼낸 노드가 오른쪽 맨 아래 좌표에 도달하면 성공 (d 츨력)
		// 큐에서 다 꺼냈는데도 도달하지 못했으면 -1 출력
		
		while(!q.isEmpty()) {
			Node node = q.poll();
			
			if(node.y == h - 1 && node.x == w - 1) {  // 목표 도달
				System.out.println(node.d);
				return;
			}
			
			// #1. 상하좌우
			for (int[] d : direction) {
				int ny = node.y + d[0];
				int nx = node.x + d[1];
				if(ny < 0 || nx < 0 || ny >= h || nx >= w || map[ny][nx] == 1 || visit[ny][nx][node.k]) 
					continue;
				visit[ny][nx][node.k] = true;
				q.offer(new Node(ny, nx, node.k, node.d + 1));
			}
			
			if(node.k == 0) {  // k를 다 사용했다면
				continue;
			}
			
			// 말 - 격자 - 8방
			for (int[] h_d : h_direction) {
				int ny = node.y + h_d[0];
				int nx = node.x + h_d[1];
				if(ny < 0 || nx < 0 || ny >= h || nx >= w || map[ny][nx] == 1 || visit[ny][nx][node.k - 1]) 
					continue;
				visit[ny][nx][node.k - 1] = true;
				q.offer(new Node(ny, nx, node.k - 1, node.d + 1));  // 말 격자로 이동 x -> k는 그대로
				// 앞으로 k를 소모할 것이기 때문
			}
			
		}
		System.out.println(-1);
	}
	
	static class Node {
		int y, x, k, d;
		Node(int y, int x, int k, int d) {
			this.y = y;
			this.x = x;
			this.k = k;
			this.d = d;
		}
	}

}
