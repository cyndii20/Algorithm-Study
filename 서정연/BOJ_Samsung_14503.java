import java.util.*;
import java.io.*;

public class BOJ_Samsung_14503 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine(), " ");
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());

		int[][] room = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				room[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int count = 0;
		boolean stop = false;
		while (!stop) {

			if (room[r][c] == 0) {
				room[r][c] = -1;
				count++;
				System.out.println("청소함");
			}

			if (room[r][c - 1] != 0 && room[r][c + 1] != 0 && room[r - 1][c] != 0 && room[r + 1][c] != 0) {
				switch (d) {
					case 0:
						if (room[r + 1][c] == 1) {
							System.out.println("작동 멈춤");
							stop = true;
						} else {
							System.out.println("청소기 후진");
							r += 1;
						}
						break;
					case 1:
						if (room[r][c - 1] == 1) {
							System.out.println("작동 멈춤");
							stop = true;
						} else {
							System.out.println("청소기 후진");
							c -= 1;
						}
						break;
					case 2:
						if (room[r - 1][c] == 1) {
							System.out.println("작동 멈춤");
							stop = true;
						} else {
							System.out.println("청소기 후진");
							r -= 1;
						}
						break;
					case 3:
						if (room[r][c + 1] == 1) {
							System.out.println("작동 멈춤");
							stop = true;
						} else {
							System.out.println("청소기 후진");
							c += 1;
						}
						break;
				}
			} else {
				boolean moved = false;
				while (!moved) {
					if (moved) {
						System.out.println("청소기 이동,  r : " + r + ", c" + c);
						break;
					}
					d = (d + 3) % 4;
					switch (d) {
						case 0:
							if (room[r - 1][c] == 0) {
								r -= 1;
								moved = true;
							}
							break;
						case 1:
							if (room[r][c + 1] == 0) {
								c += 1;
								moved = true;
							}
							break;
						case 2:
							if (room[r + 1][c] == 0) {
								r += 1;
								moved = true;
							}
							break;
						case 3:
							if (room[r][c - 1] == 0) {
								c -= 1;
								moved = true;
							}
							break;
					}
				}

			}
		}
		System.out.print(count);
	}
}
