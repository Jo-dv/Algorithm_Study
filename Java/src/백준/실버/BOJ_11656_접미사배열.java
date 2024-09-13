package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;

public class BOJ_11656_접미사배열 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static String s;
	static TreeSet<String> suffix = new TreeSet<>();
	
	public static void main(String[] args) throws IOException {
		s = br.readLine();
		
		solve();
	}
	
	static void solve() {
		int len = s.length();
		for(int i = 0; i < len; i++)
			suffix.add(s.substring(i));
		
		for(String i: suffix)
			System.out.println(i);
	}
}
