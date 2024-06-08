import java.io.*;
import java.util.*;

public class BOJ_19532 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();
        
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int f = Integer.parseInt(st.nextToken());
        int x = 0;
        int y = 0;
        
        for(x = -999; x <= 999; x++){
            for(y = -999; y <= 999; y++){
                if((a*x + b*y == c) && (d*x + e*y == f)) {
                    sb.append(x).append(" ").append(y);
                    break;
                }
            }
        }
        
        System.out.print(sb);

	}

}

