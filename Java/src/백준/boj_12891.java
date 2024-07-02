package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.StringTokenizer;

public class boj_12891 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int s = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
		String dna = br.readLine();
		st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int g = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int t = Integer.parseInt(st.nextToken());
		int start = 0;
		int end = p - 1;
		LinkedHashMap<String, Integer> dict = new LinkedHashMap<String, Integer>(); 
		dict.put("A", 0);
		dict.put("C", 0);
		dict.put("G", 0);
		dict.put("T", 0);
		
		while(end < s) {
			String k1 = String.valueOf(dna.charAt(start));
			String k2 = String.valueOf(dna.charAt(end));
			dict.put(k1, dict.get(k1) + 1);
			dict.put(k2, dict.get(k2) + 1);
			start++;
			end++;
		}
	System.out.println(dict.values());
	}

}
