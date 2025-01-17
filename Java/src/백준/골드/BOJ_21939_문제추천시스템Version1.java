package 백준.골드;

import java.io.*;
import java.util.*;

public class BOJ_21939_문제추천시스템Version1 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        TreeMap<Integer, TreeSet<Integer>> problems = new TreeMap<>();  // 난이도 -> 문제 번호
        Map<Integer, Integer> problem_map = new HashMap<>(); // 문제 번호 -> 난이도

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            problems.putIfAbsent(l, new TreeSet<>());
            problems.get(l).add(p);
            problem_map.put(p, l);
        }

        int m = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            String[] line = br.readLine().split(" ");
            String command = line[0];

            if (command.equals("recommend")) {
                int x = Integer.parseInt(line[1]);

                if (x == 1) { // 가장 어려운 문제
                    int max_difficulty = problems.lastKey();
                    int maxProblem = problems.get(max_difficulty).last();
                    sb.append(maxProblem).append("\n");
                } else { // 가장 쉬운 문제
                    int minDifficulty = problems.firstKey();
                    int minProblem = problems.get(minDifficulty).first();
                    sb.append(minProblem).append("\n");
                }
            } else if (command.equals("add")) {
                int p = Integer.parseInt(line[1]);
                int l = Integer.parseInt(line[2]);

                problems.putIfAbsent(l, new TreeSet<>());
                problems.get(l).add(p);
                problem_map.put(p, l);
            } else if (command.equals("solved")) {
                int p = Integer.parseInt(line[1]);
                int l = problem_map.get(p);

                problems.get(l).remove(p);
                if (problems.get(l).isEmpty()) {
                    problems.remove(l);
                }
                problem_map.remove(p);
            }
        }

        System.out.print(sb);
    }
}

