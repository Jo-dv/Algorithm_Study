package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_1525_퍼즐 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static String target = "123456780";
    
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();  // 배열을 일렬로 입력
        for(int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 3; j++)
                sb.append(st.nextToken());
        }
        String start = sb.toString();
        System.out.println(solve(start));
    }
    
    static int solve(String start) {
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.move - o2.move);  // 최단 횟수 보장
        HashSet<String> visited = new HashSet<>();
        pq.add(new Node(start, 0));
        visited.add(start);
        
        while(!pq.isEmpty()) {
            Node current = pq.poll();
            String currentState = current.state;  // 현재 퍼즐 상태
            int move = current.move;  // 현재 퍼즐을 만들기 위해 움직인 횟수
            
            if(currentState.equals(target))  // 정렬이 완료되었다면
                return move;
            
            int zeroIndex = currentState.indexOf('0');
            int y = zeroIndex / 3;  // 행
            int x = zeroIndex % 3;  // 열
            
            for (int[] d : directions) {
                int my = y + d[0];
                int mx = x + d[1];
                
                if(0 <= my && my < 3 && 0 <= mx && mx < 3) {  // 유효 범위 이내
                    int newZeroIndex = my * 3 + mx;  // 1차원 배열 형태의 위치로 복원
                    char[] newStateArr = currentState.toCharArray();
                    newStateArr[zeroIndex] = newStateArr[newZeroIndex];  // 위치 스왑
                    newStateArr[newZeroIndex] = '0';  // 새로운 위치에 0 삽입
                    String newState = new String(newStateArr);
                    
                    if(!visited.contains(newState)) {  // 새로운 퍼즐이 아직 등록되어있지 않으면
                        visited.add(newState);
                        pq.add(new Node(newState, move + 1));  // // 해당 퍼즐을 만들기 위해 한 번 움직였으므로
                    }
                }
            }
        }
        
        return -1;
    }
    
    static class Node {
        String state;
        int move;
        
        Node(String state, int move) {
            this.state = state;
            this.move = move;
        }
    }
}
