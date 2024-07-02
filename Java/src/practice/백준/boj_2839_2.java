package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// Greedy
// 3보다는 5를 사용해야 유리
// 5를 사용할 때는 최대한 많이, 3을 많이 사용할 때는 최대한 적게
// 5로 나누어 지는 상황 -> 5로 나눔
// 3 빼기, 나누기...
public class boj_2839_2 {
	static int n;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());

		int count = 0;  // 사용한 봉투의 수
		while(true) {
			if(n < 0) {
				System.out.println(-1);
				break;
			}
			
			if(n % 5 == 0)  { // 5짜리를 최대한 많이 사용하기 위해 나누어 떨어지면 나눈다.
				System.out.println(n/5 + count);
				break;
			}
			else {  // 5로 나눠 떨어지지 않으면 3만큼 줄인다.
				n -= 3;
				count++;
			}
		}
	}
}
