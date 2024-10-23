import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        BufferedReader reader = new BufferedReader(new FileReader("day03/BOJ2309/input.txt"));
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> lst = new ArrayList<>();
        int total = 0;
        
        for (int i = 0; i < 9; i++) {
            int elem = Integer.parseInt(reader.readLine());
            lst.add(elem);
            total += elem;
        }

        Collections.sort(lst);

        List<Integer> toSubtract = new ArrayList<>();
        int gapWithTotal = total - 100;
        int first = -1;
        int second = -1;
        boolean found = false;

        for (int i = 0; i < 9 && !found; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (lst.get(i) + lst.get(j) == gapWithTotal) {
                    first = i;
                    second = j;
                    found = true;
                    break;
                }
            }
        }

        for (int i = 0; i < 9; i++) {
            if (i != first && i != second) {
                System.out.println(lst.get(i));
            }
        }
    }
}