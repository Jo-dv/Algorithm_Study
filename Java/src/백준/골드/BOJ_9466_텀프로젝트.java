package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_9466_텀프로젝트 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int t;
    static int n;
    static int[] students;
    static boolean[] visited;
    static boolean[] done;
    static StringBuilder sb = new StringBuilder();
    static int count;

    public static void main(String[] args) throws IOException {
        t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            students = new int[n + 1];
            visited = new boolean[n + 1];
            done = new boolean[n + 1];
            count = 0;

            for (int i = 1; i <= n; i++)
                students[i] = Integer.parseInt(st.nextToken());

            solve();
        }

        System.out.println(sb);
    }

    static void solve() {
        for (int i = 1; i <= n; i++)
            if (!visited[i])
                dfs(i);

        sb.append(n - count).append("\n");
    }

    static void dfs(int current) {
        visited[current] = true;
        int next = students[current];  // 다음 노드

        if (!visited[next])  // 다음 노드를 아직 방문하지 않았다면
            dfs(next);
        else if (!done[next])  // 사이클 확인
            find_cycle(next);

        done[current] = true;  // 사이클 탐색 종료
    }

    static void find_cycle(int start) {
        count++;  // 자기 자신
        for (int i = students[start]; i != start; i = students[i])  // 다음 노드가 주어진 start와 다르면
            count++;
    }
}
