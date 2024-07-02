package practice.swea;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class swea_3124 {
	static int v, e;
	static int[][] edges;
	static int[] parent;
	static int cnt;
	static long answer;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc <= t; tc++) {
			st = new StringTokenizer(br.readLine());
			v = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			edges = new int[e][3];
			parent = new int[v + 1];
			cnt = 0;
			answer = 0;
			
			makeset();
			for(int i = 0; i < e; i++) {
				st = new StringTokenizer(br.readLine());
				edges[i][0] = Integer.parseInt(st.nextToken());
				edges[i][1] = Integer.parseInt(st.nextToken());
				edges[i][2] = Integer.parseInt(st.nextToken());
			}
			Arrays.sort(edges, (o1, o2) -> o1[2] - o2[2]);
			for (int[] i : edges) {
				System.out.println(Arrays.toString(i));
			}
			for(int i = 0; i < e; i++)
				if(union(edges[i][0], edges[i][1])) {
					answer += edges[i][2];
					cnt++;
					if(cnt == v - 1) 
						break;
				}
			
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		
		System.out.println(sb);
	}
	
	static void makeset() {
		for(int i = 1; i <= v; i++) parent[i] = i;
	}
	
	static int find(int x) {
		if(parent[x] == x)
			return x;
		else
			return parent[x] = find(parent[x]);
	}
	
	static boolean union(int x, int y) {
		int px = find(x);
		int py = find(y);
		if(px == py)
			return false;
		parent[py] = px;
		return true;
	}

}