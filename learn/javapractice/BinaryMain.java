//Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
//The returned integer should be non-negative as well.
//You must not use any built-in exponent function or operator.

public class BinaryMain {

  public static void main(String[] args) {
    int x = 1000000000;
    int answer = solution(x);
    System.out.println(answer);
  }

  private static int solution(int input) {
    return sqrt_binary_search(input);
  }

  private static int sqrt_binary_search(int input) {

    if (input == 0 || input == 1) {
      return input;
    }

    int left = 1;
    int right = input;

    int ans = 0;

    while (left <= right) {
      // find mid
      int mid = left + (right - left) / 2;

      if (mid == input / mid) {
        return mid;
      }

      else if (mid < input / mid) {
        ans = mid;
        left = mid + 1;
      } else {
        right = mid - 1;
      }

    }
    return ans;

  }
}
