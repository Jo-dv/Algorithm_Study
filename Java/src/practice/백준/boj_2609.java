package practice.boj;

import java.util.Scanner;

public class boj_2609 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int gcd = cal_gcd(a, b);
		int lcm = (a * b) / gcd ;
		System.out.println(gcd);
		System.out.println(lcm);
	}
	
	static int cal_gcd(int a, int b) {
		if(b == 0)
			return a;
		return cal_gcd(b, a % b);
	}
}