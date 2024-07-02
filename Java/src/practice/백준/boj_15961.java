package practice.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_15961 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int[] dishes = new int[n + k];
		int[] eat = new int[d + 1];
		int max_kind = 0;
		int answer = 0;
		for (int i = 0; i < n; i++)
			dishes[i] = Integer.parseInt(br.readLine());

		for (int i = n; i < n + k; i++) // 처음 입력에서 k개만큼 원 배열에 추가하여 한 회전 세트 생성
			dishes[i] = dishes[i - n];

		for (int i = 0; i < k; i++) { // 첫 k 접시
			eat[dishes[i]]++; // 해당 종류에 해당 하는 초밥을 먹을 때마다 값 갱신
			if (eat[dishes[i]] == 1) // 초밥을 먹었을 때 처음 먹어본 것이라면
				max_kind++; // 먹어본 초밥의 종류 추가
		}
		answer = max_kind; // 처음 k 접시는 처음이자 최대

		int s = 0, e = k; // k 개의 접시 중 가장 선두와 후미

		while (e < n + k - 1) { // 모든 세트를 다 볼 때까지
			eat[dishes[e]]++; // 새로운 접시 섭취
			if (eat[dishes[e]] == 1) // 해당 초밥이 처음 먹는 것일 경우
				max_kind++; // 종류 추가
			eat[dishes[s]]--; // k 개의 접시를 맞추기 위해 앞서 먹었던 것 제거
			if (eat[dishes[s]] == 0) // 만약 제거했을 때 안 먹어본 상태로 돌아간다면
				max_kind--; // 종류 감소
			if (eat[c] == 0) { // 섭취한 초밥 중 쿠폰에 해당하는 초밥을 처음 먹어보는 경우
				eat[c]++;
				max_kind++; // 종류 추가
				answer = max_kind > answer ? max_kind : answer; // 하나의 검사가 끝났을 때 값 갱신
				s++; // 다음 탐색을 위해 탐색 인덱스 조정
				e++;
			}
			System.out.println(answer);
		}
	}

}
