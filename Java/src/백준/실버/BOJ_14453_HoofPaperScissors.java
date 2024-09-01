package 백준.실버;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_14453_HoofPaperScissors {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static String[] gestures;
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		gestures = new String[n];
		for(int i = 0; i < n; i++)
			gestures[i] = br.readLine();
		
		solve();
	}
	
	static void solve() {
		int[] h_prefix = new int[n + 1];
        int[] p_prefix = new int[n + 1];
        int[] s_prefix = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            h_prefix[i] = h_prefix[i - 1];
            p_prefix[i] = p_prefix[i - 1];
            s_prefix[i] = s_prefix[i - 1];
            
            h_prefix[i] += (gestures[i - 1].equals("H") ? 1 : 0);
            p_prefix[i] += (gestures[i - 1].equals("P") ? 1 : 0);
            s_prefix[i] += (gestures[i - 1].equals("S") ? 1 : 0);
        }
        
        for (int i = 0; i <= n; i++) {
            // p를 내다가 s, h로 바꾸는 경우
            int ps = h_prefix[i] + (p_prefix[n] - p_prefix[i]);
            int ph = h_prefix[i] + (s_prefix[n] - s_prefix[i]);

            // s를 내다가 p, h로 바꾸는 경우
            int sp = p_prefix[i] + (h_prefix[n] - h_prefix[i]);
            int sh = p_prefix[i] + (s_prefix[n] - s_prefix[i]);

            // h를 내다가 p, s로 바꾸는 경우
            int hp = s_prefix[i] + (h_prefix[n] - h_prefix[i]);
            int hs = s_prefix[i] + (p_prefix[n] - p_prefix[i]);

            answer = Math.max(answer, Math.max(ps, Math.max(ph, Math.max(sp, Math.max(sh, Math.max(hp, hs))))));
        }
	}

}
