package 백준;

import java.util.Arrays;
import java.util.Scanner;

public class boj_11650 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Integer[][] cord = new Integer[n][2];
		for(int i = 0; i < n; i++) {
			cord[i][0] = sc.nextInt();
			cord[i][1] = sc.nextInt();
		}
		Arrays.sort(cord, (o1, o2) -> (o1[0] == o2[0]) ? o1[1].compareTo(o2[1]) : o1[0].compareTo(o2[0]));
		
		for (Integer[] c : cord) {
			System.out.println(c[0] + " " + c[1]);
		}
	}
}
