import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        BufferedReader reader = new BufferedReader(new FileReader("day04/BOJ1978/input.txt"));
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(reader.readLine());
        String[] input = reader.readLine().split(" ");

        List<Integer> lst = new ArrayList<>();
        for (String s : input) {
            lst.add(Integer.parseInt(s));
        }

        int answerCnt = 0;
        for (int num : lst) {
            boolean isPrime = true;

            if (num < 2) {
                isPrime = false;
            }

            for (int i = 2; i < num; i++) {
                if (num % i == 0) {
                    isPrime = false;
                }
            }

            if (isPrime == true) {
                answerCnt += 1;
            }
        }

        System.out.println(answerCnt);
    }
}
