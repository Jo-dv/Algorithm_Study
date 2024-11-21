package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_18430_무기공학 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m, answer = 0;
    static int[][] wood;
    static boolean[][] used;
    static int[][][] boomerangs = {  // 부메랑의 4가지 형태를 표현 (중심 포함)
        {{0, 0}, {1, 0}, {0, 1}}, // 「 
        {{0, 0}, {0, 1}, {-1, 0}}, // ㄱ
        {{0, 0}, {-1, 0}, {0, -1}}, // 」
        {{0, 0}, {0, -1}, {1, 0}} // ㄴ
    };

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        wood = new int[n][m];
        used = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                wood[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solve(0, 0, 0);
        System.out.println(answer);
    }

    static void solve(int y, int x, int value) {
        if (y == n) {  // 모든 칸을 탐색 완료했으면 종료
            answer = Math.max(answer, value);
            return;
        }

        // 다음 칸으로 이동
        int next_y = (x + 1 == m) ? y + 1 : y;
        int next_x = (x + 1 == m) ? 0 : x + 1;

        solve(next_y, next_x, value);  // 현재 칸을 사용하지 않고 다음 칸으로 이동

        if (!used[y][x]) {  // 현재 칸을 중심으로 부메랑을 만들어봄
            for (int[][] boomerang : boomerangs) {
                int strength = 0;
                boolean valid = true;

                for (int[] offset : boomerang) {  // 부메랑의 모든 칸을 확인
                    int my = y + offset[0];
                    int mx = x + offset[1];
                    if (my < 0 || mx < 0 || my >= n || mx >= m || used[my][mx]) {  // 범위를 벗어나거나 이미 사용된 칸이면 불가능
                        valid = false;
                        break;
                    }
                }

                if (valid) {  // 부메랑 배치
                    for (int[] offset : boomerang) {
                        int my = y + offset[0];
                        int mx = x + offset[1];
                        strength += (offset[0] == 0 && offset[1] == 0) ? wood[my][mx] * 2 : wood[my][mx];
                        used[my][mx] = true;
                    }

                    solve(next_y, next_x, value + strength);  // 다음 칸 탐색
                    
                    for (int[] offset : boomerang) {  // 부메랑 해제
                        int my = y + offset[0];
                        int mx = x + offset[1];
                        used[my][mx] = false;
                    }
                }
            }
        }
    }
}
