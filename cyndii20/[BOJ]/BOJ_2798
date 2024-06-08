import java.io.*;
import java.util.*;

public class BOJ_2798{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine(), " ");
        int[] numbers = new int[N];
        for(int i = 0; i < N; i++){
            numbers[i] = Integer.parseInt(st.nextToken());
        }
        
        int sum = 0;
        int max = 0;
        for(int i = 0; i + 2 < N; i++){
            for(int j = i + 1; j + 1 < N ; j++){
                for(int k = j + 1; k < N; k++) {
                	sum = numbers[i] + numbers[j] + numbers[k];
                	if(sum > max && sum <= M) {
                     	max = sum;
                	}
                }
            }
        }
        System.out.print(max);
    }
}
