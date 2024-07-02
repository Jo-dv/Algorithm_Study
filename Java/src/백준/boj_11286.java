package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class boj_11286 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		PriorityQueue<Integer> arr = new PriorityQueue<Integer>((o1, o2) -> (Math.abs(o1) == Math.abs(o2) ? o1 - o2 : Math.abs(o1) - Math.abs(o2)));
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++ ) {
			int x = Integer.parseInt(br.readLine());
			
			if(x != 0)
				arr.add(x);
			else
				sb.append(arr.isEmpty() ? 0 : arr.poll()).append("\n");
		}
		System.out.println(sb);
	}
}
