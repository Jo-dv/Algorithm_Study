package practice.swea;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class swea_1247 {
	static int n;
	static int[] home;
	static int[] company;
	static int[][] clients;
	static int[] res;
	static boolean[] visit;
	static List<int[]> des;
	static int answer;
	static int distance;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			home = new int[2];
			company = new int[2];
			clients = new int[n][2];
			visit = new boolean[n];
			res = new int[n];
			des = new ArrayList<int[]>();
			answer = Integer.MAX_VALUE;
			st = new StringTokenizer(br.readLine());
			company[0] = Integer.parseInt(st.nextToken());
			company[1] = Integer.parseInt(st.nextToken());
			home[0] = Integer.parseInt(st.nextToken());;
			home[1] = Integer.parseInt(st.nextToken());;
			for(int i = 0; i < n; i++) {
				clients[i][0] = Integer.parseInt(st.nextToken());;
				clients[i][1] = Integer.parseInt(st.nextToken());;
			}
			
			perm(0);
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
	
	static void perm(int target) {
		if(target == n) {
			distance = cal_distance(company[0], company[1], clients[res[0]][0], clients[res[0]][1]);
			for(int i = 0; i < n - 1; i++) 
				distance += cal_distance(clients[res[i]][0], clients[res[i]][1], clients[res[i + 1]][0], clients[res[i + 1]][1]);
			distance += cal_distance(clients[res[n-1]][0], clients[res[n-1]][1], home[0], home[1]);
			answer = distance < answer ? distance : answer;
			return;
		}
		for(int i = 0; i < n; i++) {
			if(visit[i])
				continue;
			res[target] = i;
			visit[i] = true;
			perm(target + 1);
			visit[i] = false;
		}
	}
	
	static int cal_distance(int x1, int y1, int x2, int y2) {
		return Math.abs(x1 - x2) + Math.abs(y1 - y2);
	}

}