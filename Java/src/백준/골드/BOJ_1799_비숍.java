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
    static int[][] directions = {{-1, -1}, {1, -1}, {-1, 1}, {1, 1}};
    static List<int[]> white = new ArrayList<>();
    static List<int[]> black = new ArrayList<>();
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
                    if ((y + x) % 2 == 0)  // 흑백은 서로 간섭하지 못하는 영역이므로 각각을 나눠서 체크함
                        white.add(new int[]{y, x});
                    else
                        black.add(new int[]{y, x});
    }
    
	static boolean check(int y, int x) {  // 가능한 구역에 9(비숍)이 있는지 확인
		for(int[] d: directions) {
			int my = y + d[0];
			int mx = x + d[1];
			
			while(0 <= my && my < size && 0 <= mx && mx < size) {
				if(board[my][mx] == 9)
					return false;
				my += d[0];
				mx += d[1];
			}
		}
		
		return true;
	}

    static void search(int idx, int count, List<int[]> bishops, boolean is_black) {
        if (idx == bishops.size()) {
            if (is_black)
                answer[1] = Math.max(answer[1], count);
            else
                answer[0] = Math.max(answer[0], count);
            
            return;
        }

        int y = bishops.get(idx)[0];
        int x = bishops.get(idx)[1];

        if (check(y, x)) {
        	board[y][x] = 9;
            search(idx + 1, count + 1, bishops, is_black);
            board[y][x] = 1;
        }

        search(idx + 1, count, bishops, is_black);  // 현재 위치에 두지 않는 경우도 고려
    }

    static void solve() {
        find_bishops();
        search(0, 0, white, false);
        search(0, 0, black, true);
    }
}