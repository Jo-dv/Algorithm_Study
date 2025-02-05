package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_20208_진우의민트초코우유 {
    static int N, M, H;
    static int[][] map;
    static boolean[] visited;
    static int homeY, homeX;
    static List<int[]> milks = new ArrayList<>();
    static int maxMilk = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        map = new int[N][N];

        // 지도 입력 받기 및 집과 민트초코우유 위치 저장
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    homeY = i;
                    homeX = j;
                } else if (map[i][j] == 2) {
                    milks.add(new int[]{i, j});
                }
            }
        }

        visited = new boolean[milks.size()];
        dfs(homeY, homeX, M, 0);

        System.out.println(maxMilk);
    }

    // 백트래킹 DFS 탐색
    static void dfs(int y, int x, int hp, int count) {
        // 집으로 돌아올 수 있는 경우만 유효한 경로로 인정
        if (Math.abs(y - homeY) + Math.abs(x - homeX) <= hp) {
            maxMilk = Math.max(maxMilk, count);
        }

        for (int i = 0; i < milks.size(); i++) {
            if (!visited[i]) {
                int ny = milks.get(i)[0];
                int nx = milks.get(i)[1];
                int dist = Math.abs(y - ny) + Math.abs(x - nx); // 거리 계산

                if (dist <= hp) { // 이동 가능한 경우
                    visited[i] = true;
                    dfs(ny, nx, hp - dist + H, count + 1);
                    visited[i] = false;
                }
            }
        }
    }
}
