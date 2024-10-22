import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] numbers = br.readLine().split(" ");
        int a = Integer.parseInt(numbers[0]);
        int b = Integer.parseInt(numbers[1]);

        int i = 2;
        int result1 = 1;
        while (true) {
            if (a % i == 0 && b % i == 0) {
              a /= i;
              b /= i;
              result1 *= i;
            } else if (a % i != 0 || b % i != 0){
                i++;
            }
            if (a < i && b < i) {
                int result2;
                result2 = result1 * a * b;
                System.out.println(result1);
                System.out.println(result2);
                return;
            }
        }

    }
}
