package practice.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_5607 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int mod = 1234567891;
	static int n, r;
	static int t;
	static long[] facto;
	static long denominator, numerator, modi_numerator;
	static long answer;

	public static void main(String[] args) throws Exception {
		t = Integer.parseInt(br.readLine());
		facto = new long[1000000 + 1];
		facto[0] = 1;
		for (int i = 1; i <= 1000000; i++)
			facto[i] = (facto[i - 1] * i) % mod;

		for (int tc = 1; tc <= t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			r = Integer.parseInt(st.nextToken());
			answer = 0;

			denominator = facto[n] % mod;
			numerator = ((facto[n - r] % mod) * (facto[r] % mod)) % mod;
			modi_numerator = powCalc(numerator, mod - 2);
			answer = (denominator * modi_numerator) % mod;

			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}

	static long powCalc(long num, int p) {
		if (p == 0)
			return 1;

		long half = powCalc(num, p / 2);

		if (p % 2 == 0) {
			return ((half % mod) * (half % mod)) % mod;
		} else
			return (((half * num) % mod) * (half % mod)) % mod;
	}
}