package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_11404 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
    static int n, m;
    static int a, b, c;
    static int[][] graph;
    
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        graph = new int[n][n];

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                graph[i][j] = i == j ? 0 : 100000 * 100;

        for(int j = 0; j < m; j++) {
        	st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            graph[a-1][b-1] = Math.min(graph[a-1][b-1], c);  // 동일 경로 최소 비용 선택
        }
        
        solve();
    }

    static void solve() {
        for(int k = 0; k < n; k++) {
            for(int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                    if(graph[i][k] + graph[k][j] < graph[i][j])
                        graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }

        for(int[] i : graph) {
            for(int j : i)
            	sb.append(j != 100000 * 100 ? j : 0).append(" ");
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
