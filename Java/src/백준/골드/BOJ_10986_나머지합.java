package 백준.골드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10986_나머지합 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m;
    static int[] arr;
    
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(solve());
    }

    static long solve() {
        long answer = 0;
        long sum = 0;
        long[] count = new long[m];  // 나머지 m으로 나눈 값의 개수를 저장할 배열
        count[0] = 1;  // sum % m == 0인 경우를 고려

        for (int i = 0; i < n; i++) {
            sum += arr[i]; 
            int remainder = (int) (sum % m);  // 누적 합의 나머지
            
            answer += count[remainder]++;  // 같은 나머지가 나온 횟수만큼 더함
        }

        return answer;
    }
}
