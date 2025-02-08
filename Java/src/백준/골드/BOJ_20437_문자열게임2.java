package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_20437_문자열게임2 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int t;
    static String w;
    static int k;
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        t = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < t; i++) {
            w = br.readLine();
            k = Integer.parseInt(br.readLine());
            solve();
        }

        System.out.println(sb);
    }
    
    static void solve() {
        HashMap<Character, List<Integer>> dict = new HashMap<>();
        
        for (int i = 0; i < w.length(); i++) {  // 각 문자에 대한 등장 위치 저장
            char key = w.charAt(i);
            dict.putIfAbsent(key, new ArrayList<>());
            dict.get(key).add(i);
        }
        
        int minLen = Integer.MAX_VALUE;
        int maxLen = -1;
        
        for (List<Integer> positions : dict.values()) {  // 등장 위치 기반으로 연속 부분 문자열 길이 계산
            if (positions.size() < k) {
            	continue;
            }
            
            for (int i = 0; i <= positions.size() - k; i++) {
                int len = positions.get(i + k - 1) - positions.get(i) + 1;  // k번째 등장 위치 - 시작 위치
                minLen = Math.min(minLen, len);
                maxLen = Math.max(maxLen, len);
            }
        }
        
        if (minLen == Integer.MAX_VALUE) {
            sb.append(-1).append("\n");
        } else {
            sb.append(minLen).append(" ").append(maxLen).append("\n");
        }
    }
}
