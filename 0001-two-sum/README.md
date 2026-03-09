You've provided two excellent approaches to the Two Sum problem: a straightforward brute-force solution and an optimized hash map solution. Both are clearly explained in your comments!

Here's a clean, well-formatted README for your code:

---

# LeetCode: Two Sum

## Problem Explanation

The "Two Sum" problem challenges us to find two distinct numbers within a given array of integers, `nums`, that sum up to a specific `target` integer. The goal is to return the **indices** of these two numbers.

Key constraints and assumptions for this problem are:
*   There will always be exactly one valid solution.
*   We cannot use the same element twice (meaning we must pick two numbers at different indices).
*   The order of the returned indices does not matter.

## My Solutions

I've implemented two solutions: a brute-force approach (currently active in the code) and a more optimal solution utilizing a hash map (commented out).

### 1. Brute-Force Approach (Accepted Code)

This approach checks every possible pair of numbers in the array to see if their sum equals the target.

#### Step-by-Step Explanation

1.  **Outer Loop (`i`):** We iterate through the array `nums` with an index `i` from the first element up to the second-to-last element (`len(nums) - 1`).
2.  **Inner Loop (`j`):** For each `i`, we start a nested loop with an index `j` from `i + 1` up to the last element (`len(nums) - 1`).
    *   Starting `j` from `i + 1` ensures that we only consider unique pairs of indices (we don't check `(0, 1)` and then `(1, 0)`) and, crucially, that we don't use the same element twice (since `j` will always be different from `i`).
3.  **Sum Check:** Inside the inner loop, we check if the sum of the numbers at `nums[i]` and `nums[j]` is equal to the `target`.
4.  **Return:** If the sum matches the `target`, we've found our pair. Since the problem guarantees exactly one solution, we immediately return a list containing their indices: `[i, j]`.

#### Complexity Analysis

##### Time Complexity
*   **O(n²)**: The outer loop runs `n-1` times, and the inner loop runs approximately `n-1` times in its first iteration, then `n-2`, and so on. This results in roughly `(n-1) + (n-2) + ... + 1 = n * (n-1) / 2` comparisons. As `n` grows, the `n²` term dominates, making the time complexity quadratic.

##### Space Complexity
*   **O(1)**: We only use a few constant variables (`i`, `j`, `nums[i]`, `nums[j]`) regardless of the input array size. No additional data structures are allocated that scale with `n`.

### 2. Optimal Approach (Using Hash Map - Commented Out in Provided Code)

This approach leverages a hash map (dictionary in Python) to achieve a linear time complexity by storing previously seen numbers and their indices.

#### Step-by-Step Explanation

1.  **Initialize Hash Map:** An empty dictionary, `remainder_map`, is created. This map will store key-value pairs where the key is a `complement` (the number needed to reach the `target`) and the value is the `index` of the number that would complete that sum.
2.  **Iterate and Check:** We iterate through `nums` using `enumerate` to get both the `index` and `num` for each element.
3.  **Lookup Check:** For each `num`, we first check if `num` is already a key in `remainder_map`.
    *   If `num` is found in `remainder_map`, it means we previously encountered its `complement` (`target - num`), and its index was stored under `num`. We've found our pair! We return `[index, remainder_map[num]]`.
4.  **Store Complement:** If `num` is *not* in `remainder_map`, it means we haven't found its partner yet. We calculate the `complement` needed for the current `num` to reach the `target` (`complement = target - num`). We then store this `complement` as a key in `remainder_map` with the current `index` as its value (`remainder_map[complement] = index`). This way, if a future number matches this `complement`, we can quickly retrieve the current `index`.

#### Complexity Analysis

##### Time Complexity
*   **O(n)**: We iterate through the `nums` array only once. Dictionary operations (insertion and lookup using the `in` operator) take an average of `O(1)` time. Therefore, the total time complexity is proportional to the number of elements `n`, making it linear.

##### Space Complexity
*   **O(n)**: In the worst-case scenario, if the solution pair is found towards the end of the array, the `remainder_map` might store up to `n-1` key-value pairs. This linear storage requirement makes the space complexity `O(n)`.

## Edge Cases and Considerations

The problem statement provides helpful constraints that simplify error handling:

*   **Guaranteed Solution:** "Only one valid answer exists." and "each input would have exactly one solution." This means we don't need to write code to handle cases where no solution exists or multiple solutions need disambiguation.
*   **Minimum Array Length:** "2 <= nums.length <= 104". We are assured that `nums` will always contain at least two elements, eliminating the need to handle empty arrays or arrays with a single element.
*   **Number Ranges:** "-109 <= nums[i] <= 109" and "-109 <= target <= 109". Both solutions correctly handle negative numbers, zero, and large positive/negative values for both `nums[i]` and `target`, as basic arithmetic and hash map operations are robust to these ranges.
*   **Duplicate Numbers:** The input array can contain duplicate values (e.g., `nums = [3,3], target = 6`).
    *   The brute-force solution handles this naturally by checking `nums[0]` with `nums[1]`.
    *   The hash map solution correctly finds the pair: when the first `3` (index 0) is processed, `remainder_map` gets `{3: 0}`. When the second `3` (index 1) is processed, it finds `3` in `remainder_map` and returns `[1, 0]`. Both are valid index pairs.
*   **Using Same Element Twice:** Both solutions inherently prevent using the same element at the *same index* twice.
    *   The brute-force `j` loop starts at `i+1`.
    *   The hash map approach stores complements and their indices, only returning a match when a *different* number (at a different index) completes the sum.

## Optimizations and Alternative Approaches

*   **Current Optimization:** The provided hash map approach is the most common and generally preferred optimization for this problem, significantly improving time complexity from `O(n^2)` to `O(n)`. This is typically what interviewers are looking for when they mention the "Follow-up" about `O(n^2)` complexity.

*   **Sorting + Two Pointers (O(n log n) time, O(n) or O(1) space):**
    *   An alternative approach involves sorting the array first (takes `O(n log n)` time).
    *   Then, use two pointers, one starting at the beginning (`left`) and one at the end (`right`).
    *   Move `left` rightward if `nums[left] + nums[right] < target`.
    *   Move `right` leftward if `nums[left] + nums[right] > target`.
    *   If `nums[left] + nums[right] == target`, you've found the values.
    *   **Caveat for this problem:** This method finds the *values* very efficiently. However, the problem explicitly asks for the *original indices*. If you sort the array, you lose the original indices. To fix this, you would first need to create a list of tuples like `(value, original_index)` and sort that list. This would add `O(n)` space for the new list.
    *   While `O(n log n)` is better than `O(n^2)`, the `O(n)` hash map solution is even faster in terms of time complexity for finding indices.