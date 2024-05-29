import java.util.Scanner;
import java.util.StringTokenizer;

public class BOJ_18312 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine(), " ");
        
        int N = Integer.parseInt(st.nextToken());
        String K = st.nextToken();
        
        int count = 0;
        for(int h = 0; h <= N; h++){
            for(int m = 0; m <= 59; m++){
                for(int s = 0; s <= 59; s++){
                	// K는 0도 포함하기 때문에 일의자리 수인 경우 앞에 0을 붙여줘야한다.
                	String time = ((h < 10)? "0"+h : ""+h) + ((m < 10)? "0"+m : ""+m) + ((s < 10)? "0"+s : ""+s);
                    if(time.contains(K)) count ++;
                }
            }
        }
        
        System.out.print(count);

	}

}
