package practice.boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class boj_3040 {
	static int[] arr = new int[9];
	static int[] select = new int[7];
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for(int i = 0; i < 9; i++)
			arr[i] = Integer.parseInt(br.readLine());
		search(0, 0, 0);
	}
	
	static void search(int idx, int target, int sum) {
		if(target == 7) {  // 기저 조건 -> 풀어야 하는 문제
			if(sum == 100) {
				for (int i : select)
					System.out.println(i);
			}
			return;
		}
		if(idx == 9)  // 단순 반복 종료
			return;


		select[target] = arr[idx];
		search(idx + 1, target + 1, sum + select[target]);
		search(idx + 1, target, sum);
	}
}
