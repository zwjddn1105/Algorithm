import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        BufferedReader reader = new BufferedReader(new FileReader("day04/BOJ2693/input.txt"));
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(reader.readLine());

        for (int i = 0; i < testCase; i++) {
            String[] input = reader.readLine().split(" ");
            List<Integer> lst = new ArrayList<>();
            for (String s : input) {
                lst.add(Integer.parseInt(s));
            }

            Collections.sort(lst, Collections.reverseOrder());
            System.out.println(lst.get(2));
        }

    }
}
