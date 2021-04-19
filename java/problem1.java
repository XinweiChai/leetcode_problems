import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> h = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            int n = target - nums[i];
            if (h.containsKey(n)) {
                return new int[] { h.get(n), i };
            } else {
                h.put(nums[i], i);
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

public class problem1 {
    public static void main(String[] args) {
        Solution x = new Solution();
        int[] a = { -3, 4, 3, 90 };
        for (int i : x.twoSum(a, 0)) {
            System.out.print(i + " ");
        }
    }
}
