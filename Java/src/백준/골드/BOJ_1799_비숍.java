package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_1799_비숍 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int size;
    static int[][] board;
    static List<int[]> white = new ArrayList<>();
    static List<int[]> black = new ArrayList<>();
    static int[] mask_white = new int[2];  // 0: 좌상단 - 우하단 대각선, 1: 좌하단 - 우상단 대각선
    static int[] mask_black = new int[2];
    static int[] answer = new int[2];

    public static void main(String[] args) throws IOException {
        size = Integer.parseInt(br.readLine());
        board = new int[size][size];

        for (int y = 0; y < size; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < size; x++)
                board[y][x] = Integer.parseInt(st.nextToken());
        }

        solve();
        System.out.println(answer[0] + answer[1]);
    }

    static void find_bishops() {
        for (int y = 0; y < size; y++)
            for (int x = 0; x < size; x++)
                if (board[y][x] == 1)
                    if ((y + x) % 2 == 0)
                        white.add(new int[]{y, x});
                    else
                        black.add(new int[]{y, x});
    }

    static boolean check(int y, int x, int[] mask) {
        int left = 1 << (y - x + (size - 1));  // 음수 인덱스 보정
        int right = 1 << (y + x);

        return (mask[0] & left) == 0 && (mask[1] & right) == 0;
    }

    static void placeBishop(int y, int x, int[] mask) {
        int left = 1 << (y - x + (size - 1));
        int right = 1 << (y + x);

        mask[0] |= left;
        mask[1] |= right;
    }

    static void removeBishop(int y, int x, int[] mask) {
        int left = 1 << (y - x + (size - 1));
        int right = 1 << (y + x);

        mask[0] &= ~left;
        mask[1] &= ~right;
    }

    static void search(int idx, int count, List<int[]> bishops, int[] mask, boolean is_black) {
        if (idx == bishops.size()) {
            if (is_black)
                answer[1] = Math.max(answer[1], count);
            else
                answer[0] = Math.max(answer[0], count);
            
            return;
        }

        int y = bishops.get(idx)[0];
        int x = bishops.get(idx)[1];

        if (check(y, x, mask)) {
            placeBishop(y, x, mask);
            search(idx + 1, count + 1, bishops, mask, is_black);
            removeBishop(y, x, mask);
        }

        search(idx + 1, count, bishops, mask, is_black);  //  현재 위치에 두지 않는 경우도 고려
    }

    static void solve() {
        find_bishops();
        search(0, 0, white, mask_black, false);
        search(0, 0, black, mask_white, true);
    }
}