package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_1786 {
	static StringBuilder sb = new StringBuilder();
	static String t, p;
	static int cnt;
	static int[] pi;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = br.readLine();
		p = br.readLine();
		kmp(t, p);
		System.out.println(cnt);
		System.out.println(sb);
	}
	
	static void kmp(String text, String pattern) {
		// pi 배열
		makePi(pattern);
		// 패턴 매칭
		int tLength = text.length();
		int pLength = pattern.length();
		char[] tArray = text.toCharArray();
		char[] pArray = pattern.toCharArray();
		
		int j = 0;
		for (int i = 0; i < tArray.length; i++) {
			while(j > 0 && tArray[i] != pArray[j])
				j = pi[j-1];
			// 아래 라인의 의미는 현재 text의 i번째 글자의 pattern의 j번째 글자가 일치하는 상황 => 2가지 경우가 존재
			// 모두 일치 혹은 일부 일치
			if(tArray[i] == pArray[j]) {
				if(j == pLength - 1) {  // 모두 일치
					cnt++;
					sb.append(i - j + 1).append(" ");
					j = pi[j];
				} 
				else {  // 일부 일치
					j++;  // 나머지가 일치하는지 확인하기 위해 index 하나 증가
				}
			}
		}
	}
	
	static void makePi(String p) {
		pi = new int[p.length()];
		char[] pArray = p.toCharArray();
		
		// j 접두사 쪽 인덱스. i 접미사 쪽 인덱스
		int j = 0;
		for (int i = 1; i < pArray.length; i++) {
			// i 번째 값(뒤쪽)과 j 번째 값(앞쪽)이 일치하거나, j == 0이면 while문 종료
			while(j > 0 && pArray[i] != pArray[j])
				j = pi[j-1];
			// 현재 시점은 j == 0이거나 i번째 값과 j번째 값이 일치하는 경우
			if(pArray[i] == pArray[j])
				pi[i] = ++j;
		}
	}
}
