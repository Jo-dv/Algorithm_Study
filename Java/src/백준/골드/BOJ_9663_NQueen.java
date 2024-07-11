package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_9663_NQueen {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		int[] board = new int[n];  // 행에 대한 열의 정보를 저장 -> n = 4: [1, 3, 0, 2] -> 1행 3열에 퀸이 있다. -> (0, 1), (1, 3), (3, 0), (4, 2)에 퀸이 존재
		
		System.out.println(solve(0, board));
	}
	
	static boolean is_valid(int[] board, int row, int col) {
		for (int i = 0; i < row; i++)
            if (board[i] == col || board[i] - i == col - row || board[i] + i == col + row)  // 각각 열, 대각선 확인
                return false;
        
		return true;
	}
	
	static int solve(int row, int[] board) {
		if(row == n)  // 모든 퀸을 배치했다면
			return 1;
		
		int cnt = 0;
        for (int col = 0; col < n; col++)  // 현재 행에 가능한 모든 열에 대해
            if (is_valid(board, row, col)) {  // 유효성 검사
                board[row] = col;  // 퀸 배치
                cnt += solve(row + 1, board);  // 다음 탐색
                board[row] = -1;  // 퀸 제거
            }
        
        return cnt;
	}
}
