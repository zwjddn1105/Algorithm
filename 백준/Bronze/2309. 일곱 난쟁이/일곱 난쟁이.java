import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] dwarfs = new int[9];
        int[] answer = new int[7];
        int total = 0;

        for (int i = 0; i < 9; i++) {
            int height = Integer.parseInt(br.readLine());
            dwarfs[i] = height;
            total += height;
        }

        for (int j = 0; j < 9; j++) {
            for (int k = j+1; k < 9; k++) {
                int sub = total;
                sub -= dwarfs[j];
                sub -= dwarfs[k];
                if (sub == 100){
                    int idx = 0;
                    for (int l = 0; l < 9; l++){
                        if (l != j && l != k) {
                            answer[idx] = dwarfs[l];
                            idx++;
                        }
                    }
                Arrays.sort(answer);
                for (int i = 0; i < 7; i++) {
                    System.out.println(answer[i]);
                }
                return;
                }
            }

        }

    }
}
