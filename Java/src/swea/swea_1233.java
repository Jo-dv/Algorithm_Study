package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_1233 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for (int i = 1; i < 11; i++) {
			int n = Integer.parseInt(br.readLine());
			int answer = 1;
			for (int j = 0; j < n; j++) {
				st = new StringTokenizer(br.readLine());
				st.nextToken();
				String temp_root = st.nextToken();
				if (!isDigit(temp_root))
					answer = 0;
			}
			System.out.printf("#%d %d\n", i, answer);
		}
	}

	static boolean isDigit(String value) {
		try {
			Integer.parseInt(value);
			return true;
		} catch (Exception e) {
			return false;
		}
	}
}
