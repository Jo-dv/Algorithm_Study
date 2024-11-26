package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class BOJ_7490_0만들기 {
    static ArrayList<String> results;
    static int n; 
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for (int t = 0; t < tc; t++) {
            n = Integer.parseInt(br.readLine());
            results = new ArrayList<>();
            search("1", 1, 1, 1);
            Collections.sort(results);
            for (String result : results) {
                System.out.println(result);
            }
            System.out.println();
        }
    }

    static void search(String expression, int sum, int prev, int idx) {
        if (idx == n) {
            if (sum == 0) 
            	results.add(expression);
            return;
        }

        int next = idx + 1;

        search(expression + "+" + next, sum + next, next, next);  // 이번 차례에 사용한 값을 prev로 저장
        search(expression + "-" + next, sum - next, -next, next);

        int concat = prev > 0 ? prev * 10 + next : prev * 10 - next;
        search(expression + " " + next, sum - prev + concat, concat, next);
    }
}
