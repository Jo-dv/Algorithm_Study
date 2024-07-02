package 백준;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;

public class boj_1697 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] arr = new int[100001];
		Deque<Integer> q = new ArrayDeque<Integer>(Arrays.asList(n));
		
		while(!q.isEmpty()) {
			int pos = q.poll();
			if(pos == k) {
				System.out.println(arr[pos]);
				break;
			}
			for (int i :new int[] {pos -1, pos + 1, pos * 2}) {
				if(0 <= i && i <= 100000 && arr[i] == 0) {
					arr[i] = arr[pos] + 1;
					q.add(i);
				}
			}
		}
	}
}
