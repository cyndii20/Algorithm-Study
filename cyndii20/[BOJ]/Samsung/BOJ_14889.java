import java.io.*;
import java.util.*;

public class BOJ_14889 {
	
	static int N;
	static int[][] table;
	static boolean[] visited;
	static int min = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		visited = new boolean[N];
		StringTokenizer st;
		
		table = new int[N][N];
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j < N; j++) {
				table[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		combination(0, N, N/2);
		System.out.print(min);

	}
	
	static void combination(int depth, int n, int r) {
		if(r == 0) {
			calTeamStrengthDiff();
			return;
		}
		
		if(depth == n) {
			return;
		} else {
			visited[depth] = true;
			combination(depth+1, n, r-1); // 뽑는 경우
			
			visited[depth] = false;
			combination(depth+1, n, r); // 뽑지 않는 경우
		}

	}
	
	static void calTeamStrengthDiff() {
		int firstTeamStrength = 0;
		int secondTeamStrength = 0;
		
		for(int i = 0; i < N; i++) {
			for(int j = i+1; j < N; j++) {
				if(visited[i] == true && visited[j] == true) {
					firstTeamStrength += table[i][j] + table[j][i];
				} else if(visited[i] == false && visited[j] == false) {
					secondTeamStrength += table[i][j] + table[j][i];
				}
			}
		}
		
		int difference = Math.abs(firstTeamStrength - secondTeamStrength);
		if(difference == 0) {
			System.out.print(0);
			System.exit(0); // 프로그램 종료
		}
		
		min = Math.min(difference,  min);
	}

}
