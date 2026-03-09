As an expert software engineer, I've reviewed your accepted solution for the LeetCode "Two Sum" problem. Your code demonstrates a clear understanding of both a straightforward brute-force approach and the more efficient hash map technique, which directly addresses the follow-up question regarding sub-O(n^2) time complexity.

Here's a detailed README for your solution:

---

# LeetCode: Two Sum (Easy)

## Problem Explanation

The "Two Sum" problem asks us to find two distinct numbers within a given array of integers, `nums`, that add up to a specific `target` integer. We need to return the 0-based indices of these two numbers.

**Key constraints and assumptions:**
*   Each input will have **exactly one solution**. This simplifies the problem as we don't need to handle cases with no solution or multiple solutions.
*   We **cannot use the same element twice**. This means if `nums[i]` is one of the numbers, the other must be `nums[j]` where `i != j`.
*   The answer can be returned in any order.

**Example:**
`nums = [2, 7, 11, 15]`, `target = 9`
Here, `nums[0]` (which is 2) + `nums[1]` (which is 7) equals 9. So, the output should be `[0, 1]`.

## Step-by-Step Explanation

Your provided code includes two distinct approaches: a brute-force method and an optimized hash map method.

### 1. Brute-Force Solution (Active Code)

This approach checks every possible pair of numbers in the array to see if they sum up to the target.

1.  **Outer Loop (`i`)**: The code iterates through the `nums` array using an index `i` from the first element up to the second-to-last element. This `i` represents the index of the first number in a potential pair.
2.  **Inner Loop (`j`)**: For each `i`, a nested loop iterates with an index `j` starting from `i + 1` up to the last element. This `j` represents the index of the second number. Starting `j` from `i + 1` is crucial:
    *   It ensures that `i` and `j` are always different indices, satisfying the "cannot use the same element twice" constraint.
    *   It avoids redundant checks (e.g., if `(nums[0], nums[1])` is checked, `(nums[1], nums[0])` will not be).
3.  **Sum Check**: Inside the inner loop, the sum of `nums[i]` and `nums[j]` is calculated and compared to the `target`.
4.  **Return**: If `nums[i] + nums[j]` equals `target`, the problem's condition is met. The function immediately returns a list containing `[i, j]`. Since the problem guarantees exactly one solution, this `return` statement will always be reached.

### 2. Optimal Solution - Using Hash Map (Commented Out Code)

This approach leverages a hash map (Python dictionary) to achieve much better time complexity by reducing the need for nested loops.

1.  **Initialize `remainder_map`**: An empty dictionary, `remainder_map`, is created. This map will store `(complement_value: index)` pairs. The "complement value" for a number `num` is `target - num` (i.e., the value that `num` needs to sum up to `target`).
2.  **Single Pass Iteration**: The code iterates through the `nums` array only once using `enumerate`, which provides both the `index` and the `num` itself for each element.
3.  **Check for Complement**: For each `num`:
    *   It checks if `num` is already a key in `remainder_map`.
    *   If `num` is found in `remainder_map`, it means we previously encountered its corresponding "complement" (i.e., `target - num`) and stored its index. The current `num` is that missing complement. We have found our pair!
    *   The function then returns `[index, remainder_map[num]]`. The `remainder_map[num]` value gives us the index of the number that, when combined with the current `num`, sums to `target`.
4.  **Store Complement**: If `num` is *not* found in `remainder_map`, it means we haven't yet seen its pair. We calculate the `complement` needed for the current `num` (`target - num`). We then store this `complement` as a key in `remainder_map` with its current `index` as the value: `remainder_map[target - num] = index`. This entry essentially says: "If you ever encounter `target - num` later, know that its partner `num` was found at this `index`."

## Complexity Analysis

### 1. Brute-Force Solution

*   **Time Complexity: O(n^2)**
    *   The outer loop runs `n` times (where `n` is the length of `nums`).
    *   The inner loop, in the worst case, runs approximately `n-1` times, then `n-2` times, and so on.
    *   This results in roughly `n * (n-1) / 2` operations, which simplifies to O(n^2).
    *   For an input array of 10,000 elements, this could mean up to 100 million operations, which might be slow for larger inputs.
*   **Space Complexity: O(1)**
    *   Only a constant amount of extra space is used for variables like `i`, `j`, and the return list, regardless of the input array's size.

### 2. Optimal Solution - Using Hash Map

*   **Time Complexity: O(n)**
    *   The code iterates through the `nums` array only once.
    *   Inside the loop, dictionary operations (lookup `num in remainder_map` and insertion `remainder_map[target - num] = index`) take **average O(1) time**. In the worst-case scenario (due to hash collisions), these operations could degrade to O(n), but for typical inputs and Python's hash map implementation, O(1) average case holds true.
    *   Thus, the total time complexity is proportional to `n` (number of elements), leading to O(n).
*   **Space Complexity: O(n)**
    *   In the worst case, if the desired pair is found at the very end of the array (or if the array only contains unique numbers and the pair is never found until the last iteration), the `remainder_map` might store up to `n-1` elements.
    *   Each element stored in the hash map takes constant space.
    *   Therefore, the space complexity is proportional to the number of elements in `nums`, which is O(n).

## Edge Cases

Both solutions effectively handle the problem constraints and implicit edge cases:

*   **Minimum Array Length (2)**: The problem states `nums.length >= 2`.
    *   The brute-force solution implicitly relies on this for the inner loop (`j` starting at `i+1`) to have elements to iterate over.
    *   The hash map solution naturally works with arrays of length 2 or more.
*   **Duplicate Numbers within `nums` (e.g., `[3, 3]`, `target = 6`)**: Both solutions correctly handle scenarios where `nums` contains duplicate values.
    *   The brute-force solution uses distinct indices `i` and `j`, so `nums[0]` and `nums[1]` in `[3, 3]` are treated as distinct elements.
    *   The hash map solution stores indices. For `[3, 3]`, target `6`:
        1.  When `num=3` (index `0`) is processed, `remainder_map[3]` becomes `0`.
        2.  When `num=3` (index `1`) is processed, it finds `3` in `remainder_map` and correctly returns `[1, 0]`.
*   **Negative Numbers and Large Values**: Python's arbitrary-precision integers mean that calculations with `-10^9 <= nums[i] <= 10^9` and `-10^9 <= target <= 10^9` are handled without overflow issues, and the logic remains sound regardless of the magnitude of the numbers.
*   **"Exactly One Valid Answer Exists"**: This constraint is key.
    *   It allows both algorithms to immediately return upon finding the first pair, simplifying the code.
    *   It removes the need to handle scenarios where no solution exists or multiple solutions need to be aggregated.
*   **"Cannot use the same element twice"**:
    *   Brute-force: Enforced by `j` starting at `i + 1`.
    *   Hash Map: When `num` is found in `remainder_map`, the `remainder_map[num]` gives the index of a *previously processed* element, which by definition is different from the current `index`.

## Optimizations

The commented-out hash map solution is the primary optimization for this problem, explicitly addressing the follow-up question: "Can you come up with an algorithm that is less than O(n^2) time complexity?".

*   **Hash Map Approach (O(n) time, O(n) space)**: As explained above, this method significantly reduces the time complexity from quadratic to linear. This is generally the most optimal solution for "Two Sum" when the requirement is to return indices. The trade-off is an increase in space complexity from O(1) to O(n), but this is often acceptable for the performance gain.

**Alternative (less applicable for indices): Sorting + Two Pointers**
Another approach that achieves O(n log n) time complexity is:
1.  **Sort the array**: This takes O(n log n) time.
2.  **Use two pointers**: One at the beginning, one at the end. Adjust them inward based on whether their sum is less than, greater than, or equal to the target. This takes O(n) time.
*   **Drawback**: This approach usually destroys the original indices of the numbers. To return the *original* indices, you would need to store pairs of `(value, original_index)` and sort these pairs, adding complexity and often not outperforming the direct O(n) hash map solution in terms of practical implementation and clarity when indices are required. Therefore, for this specific problem, the hash map is generally preferred.

Your code effectively showcases the standard optimal solution using a hash map, making it a complete and insightful submission for the "Two Sum" problem.