package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class swea_1228_2 {

	static int n, m;
	static ArrayList<String> list = new ArrayList<>();
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int t = 1; t < 11; t++) {
			list.clear(); // 리스트 초기화

			n = Integer.parseInt(br.readLine()); // 첫 줄
			StringTokenizer st = new StringTokenizer(br.readLine()); // 두 번째 줄
			for (int i = 0; i < n; i++)
				list.add(st.nextToken());

			m = Integer.parseInt(br.readLine()); // 세 번째 줄
			st = new StringTokenizer(br.readLine()); // 네 번째 줄

			// m개 명령어를 순차적으로 처리
			for (int i = 0; i < m; i++) {
				st.nextToken();
				int x = Integer.parseInt(st.nextToken()); // index
				int y = Integer.parseInt(st.nextToken()); // 들어갈 문자열 수
				// x 위치에 y개 만큼 문자열 추가
				int count = x + y;
				for (int j = x; j < count; j++)
					list.add(j, st.nextToken());
			}
			sb.append("#").append(t).append(" ");
			for (int i = 0; i < 10; i++)
				sb.append(list.get(i)).append(" ");
			sb.append("\n");

		}
		System.out.println(sb);

	}

}
