// Given an integer array nums of length n, 
// you want to create an array ans of length 2n where 
// ans [i] = nums [i] and 
// ans [i + n] = nums [i]
// for 0 < i < n (0-indexed).
//
// Specifically, ans is the concatenation of two nums arrays.
// Return the array ans.
//
// Example 1:
// Input: nums = [1,2,1]
// Output: [1,2,1, 1,2,1]
// Explanation: The array ans is formed as follows:
// - ans =
// [nums [0], nums [1], nums [2], nums [0], nums [1] , nums [2]]
// - ans = [1,2,1,1,2,1]

import java.util.ArrayList;
import java.util.List;

public class ConcatArray {

  public static void main(String[] args) {

    List<Integer> input = new ArrayList<>();
    input.add(1);
    input.add(2);
    input.add(1);

    List<Integer> result = new ArrayList<>();

    result.addAll(input);
    result.addAll(input);
    System.out.println(result);

  }
}
