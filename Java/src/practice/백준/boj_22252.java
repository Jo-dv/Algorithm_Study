package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class boj_22252 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static HashMap<String, PriorityQueue<Integer>> hash = new HashMap<>();  // 빠른 정보 접근을 위해 hash, 항상 최대를 뽑기 위해 pq
	static int q;
	static long answer = 0;  // 쿼리의 수가 10만, 정보의 길이가 10만, 정보의 값이 10만일 경우 int로 하면 가치의 총합이 범위를 초과하게 됨

	public static void main(String[] args) throws IOException {
		q = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < q; i++) {  // 쿼리의 수만큼
			st = new StringTokenizer(br.readLine());
			int code = Integer.parseInt(st.nextToken());
			String gorilla = st.nextToken();
			int amount = Integer.parseInt(st.nextToken());
			if (code == 1) {  // 고릴라들의 정보 초기화
				if (!hash.containsKey(gorilla))  // 해당 고릴라(키)에 대한 정보가 없다면 최대힙을 가지는 고릴라 생성
					hash.put(gorilla, new PriorityQueue<Integer>((o1, o2) -> o2 - o1));
				for (int j = 0; j < amount; j++)  // 고릴라의 정보 갱신
					hash.get(gorilla).add(Integer.parseInt(st.nextToken()));
			} else {  // 고릴라의 정보 판매
				if (hash.containsKey(gorilla)) {  // 정보를 팔 수 있는 고릴라가 있다면
					int limit = amount < hash.get(gorilla).size() ? amount : hash.get(gorilla).size();
					// 팔 수 있는 정보의 수가 사려고 하는 정보보다 많으면 사려고하는 정보만큼, 그게 아니라면 팔 수 있는 모든 정보
					for (int j = 0; j < limit; j++)
						answer += hash.get(gorilla).poll();  // 정보를 팔아서 정답 갱신
				}
			}
		}
		System.out.println(answer);
	}
}
