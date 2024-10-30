package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_3151_합이0 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[] students;
	static long answer = 0;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		students = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i ++)
			students[i] = Integer.parseInt(st.nextToken());
		
		solve();
	}
	
	static void solve() {
		Arrays.sort(students);
		long team = 0;
		
		for(int i = 0; i < n; i++) {
			int low = i + 1, high = n - 1;
			while(low < high) {
				team = students[i] + students[low] + students[high];
				if(team == 0) {
					if (students[low] == students[high]) {  // 같은 값이 여러 개인 경우 조합 수 계산
                        int count = high - low + 1;
                        answer += count * (count - 1) / 2;
                        break;
                    } else {
                        int leftCount = 1;
                        int rightCount = 1;
                        while (low + 1 < high && students[low] == students[low + 1]) {  // low와 동일한 값을 갖는 수 계산
                            leftCount++;
                            low++;
                        }
                        while (high - 1 > low && students[high] == students[high - 1]) {  // high와 동일한 값을 갖는 수 계산
                            rightCount++;
                            high--;
                        }
                        answer += (long) leftCount * rightCount;
                        low++;
                        high--;
                    }
				}
				else if(team < 0)
					low++;
				else
					high--;
			}
		}
		System.out.println(answer);
	}
}
