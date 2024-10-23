import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        BufferedReader reader = new BufferedReader(new FileReader("day03/BOJ2609/input.txt"));
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String[] input = reader.readLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        
        int gcd = getGCD(a, b);
        int lcm = a * b / gcd;

        System.out.println(gcd);
        System.out.println(lcm);
    }

    public static int getGCD(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return getGCD(num2, num1 % num2);
    }
}