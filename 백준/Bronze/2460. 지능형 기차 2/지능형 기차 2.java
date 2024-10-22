import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int person = 0;
        int result = 0;
        int i;
        for (i = 0; i < 10; i++) {
            String[] numbers = br.readLine().split(" ");
            person -= Integer.parseInt(numbers[0]);
            if (result < person) {
                result = person;
            }
            person += Integer.parseInt(numbers[1]);
            if (result < person) {
                result = person;
            }
        }
        System.out.println(result);


    }
}
