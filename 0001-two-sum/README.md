Here's a clean, well-formatted Markdown README for your "Two Sum" solution:

---

# LeetCode Problem: Two Sum

## Problem Description

The "Two Sum" problem asks us to find two distinct numbers within a given array of integers (`nums`) that add up to a specific `target` integer. We are required to return the *indices* of these two numbers.

**Key constraints and assumptions:**
*   Each input array will have exactly one valid solution.
*   We cannot use the same element twice (meaning, we need two *different* elements from the array, even if they have the same value).
*   The order of the returned indices does not matter.

**Example:**
If `nums = [2, 7, 11, 15]` and `target = 9`, the output should be `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Step-by-Step Explanation of the Solution

The provided Python solution utilizes a hash map (dictionary) to efficiently solve the problem in a single pass. The core idea is to iterate through the array, and for each number, determine its "complement" (the value needed to reach the `target`). We then check if this complement has been encountered and stored in our hash map earlier in the iteration.

Here's a detailed breakdown of the code's logic:

1.  **Initialize a Hash Map (`remainder_map`):**
    *   An empty dictionary, `remainder_map`, is created. This map will store key-value pairs where the **key is a `complement_value`** (a number we *need* to find to complete a sum) and the **value is the `index`** of the number that *needs* this complement.
    *   For instance, if `target` is 9 and we encounter the number `2` at index `0`, we will need `7` (`9 - 2`) to complete the sum. We'd then store `remainder_map[7] = 0`.

2.  **Iterate Through the Array with Indices:**
    *   The code uses `enumerate(nums)` to iterate through the `nums` array. This provides both the `index` (the current position of the number) and the `num` (the value itself) for each element.

3.  **Check for the Complement:**
    *   **`if num in remainder_map:`**: For the current `num`, the code checks if this `num` already exists as a *key* in our `remainder_map`.
        *   If `num` is a key in `remainder_map`, it signifies that we previously encountered a number whose complement was `num`. In simpler terms, the current `num` is exactly the value needed to complete the `target` sum with a number we've already processed.
        *   At this point, we have found our pair! The `current index` is one of the required indices, and the value associated with `num` in `remainder_map` (`remainder_map[num]`) is the index of its complement.
        *   The function immediately `return [index, remainder_map[num]]`.

4.  **Store Current Number's Complement for Future Checks:**
    *   **`remainder_map[target - num] = index`**: If the current `num` is *not* found as a key in `remainder_map` (meaning it's not the complement of any previously seen number), we prepare for subsequent numbers.
        *   We calculate the `complement` needed for the current `num`: `target - num`.
        *   We then add this `complement` as a key to `remainder_map`, with its value being the `index` of the current `num`. This entry effectively states: "If we later encounter `(target - num)`, we know it pairs with `num` which was found at this `index`."

5.  **Guaranteed Solution:**
    *   The problem statement guarantees that "exactly one solution exists." This means the loop will always find a pair and return the result before it finishes iterating through the entire array. Therefore, no explicit handling for a "no solution found" scenario is needed.

## Complexity Analysis

### Time Complexity: O(n)

*   The code iterates through the `nums` array exactly once.
*   Inside the loop, operations such as checking `if num in remainder_map` (hash map lookup) and `remainder_map[target - num] = index` (hash map insertion) take O(1) time on average. In the worst case, hash map operations can degrade to O(n) but this is rare with good hash functions and sufficient memory, and generally assumed O(1) for typical problem constraints.
*   Since there are `n` elements in `nums`, and each element involves a constant number of O(1) operations, the overall time complexity is linear, O(n).

### Space Complexity: O(n)

*   In the worst-case scenario, if the solution pair is found towards the end of the array, the `remainder_map` could potentially store up to `n-1` key-value pairs before the solution is found.
*   Each key-value pair consists of an integer (the complement) and an integer (its index).
*   Therefore, the space required by the `remainder_map` scales linearly with the number of elements `n` in the input array, resulting in O(n) space complexity.

## Edge Cases and Considerations

The problem statement simplifies several aspects, making the provided hash map solution particularly robust:

*   **"Exactly one solution exists"**: This simplifies the problem greatly, as we don't need to consider scenarios with multiple solutions or no solutions. The code is guaranteed to find and return a pair.
*   **"You may not use the same element twice"**: Our approach naturally handles this. When `num` is found as a key in `remainder_map`, `remainder_map[num]` gives us the *index* of an *earlier-processed* element. The current `index` and `remainder_map[num]` will always be different, thus ensuring two distinct elements (by index) are used. For example, if `nums = [3, 3], target = 6`:
    1.  When `num=3` at `index=0` is processed, `remainder_map[6-3]` (i.e., `remainder_map[3]`) is set to `0`.
    2.  When the next `num=3` at `index=1` is processed, `num` (which is `3`) is found in `remainder_map`. The function then returns `[1, remainder_map[3]]`, which is `[1, 0]`, correctly using distinct elements at different indices.
*   **Constraints on `nums.length`, `nums[i]`, and `target`**: The constraints (`2 <= nums.length <= 10^4` and values from `-10^9` to `10^9`) are well within limits for an `O(n)` solution and Python's arbitrary-precision integers and dictionary implementation.

## Optimizations and Alternative Approaches

While the provided one-pass hash map solution is considered the most optimal approach for this problem in terms of time complexity (achieving O(n)), it's beneficial to understand other methods and their trade-offs.

1.  **Brute-Force Approach:**
    *   **Logic:** Use two nested loops. The outer loop iterates from `i = 0` to `n-2`, and the inner loop iterates from `j = i+1` to `n-1`. For each pair `(nums[i], nums[j])`, check if `nums[i] + nums[j] == target`.
    *   **Time Complexity:** O(n^2). For each of `n` elements, we might iterate through up to `n-1` other elements.
    *   **Space Complexity:** O(1), as no extra data structures are used beyond a few variables.
    *   **Trade-off:** Simplest to implement but significantly slower for larger inputs. This is often the first approach, but the problem's follow-up specifically asks for something better than O(n^2).

2.  **Two-Pass Hash Map Approach:**
    *   **Logic:**
        1.  **First pass:** Iterate through the array and store each number and its index in a hash map (`num_value: index`).
        2.  **Second pass:** Iterate through the array again. For each `num` at `index i`, calculate its `complement = target - num`. Check if `complement` exists in the hash map. If it does, and its stored index is *not* `i` (to ensure distinct elements as per problem statement), then return `[i, hash_map[complement]]`.
    *   **Time Complexity:** O(n) (two passes, each O(n), so O(2n) which simplifies to O(n)).
    *   **Space Complexity:** O(n) (to store the hash map).
    *   **Trade-off:** Still O(n) time and O(n) space, similar to the one-pass approach, but slightly less efficient in practice due to two full passes over the array instead of one. The provided solution is a "one-pass" hash map approach, which is generally preferred.

3.  **Sorting and Two-Pointers Approach:**
    *   **Logic:**
        1.  Create pairs of `(value, original_index)` for each number in `nums`. This is crucial because sorting would lose the original indices.
        2.  Sort this list of pairs based on their `value`. This step typically takes O(n log n) time.
        3.  Use two pointers, `left` starting at the beginning and `right` starting at the end of the sorted list.
        4.  While `left < right`:
            *   Calculate `current_sum = sorted_list[left].value + sorted_list[right].value`.
            *   If `current_sum == target`, return `[sorted_list[left].original_index, sorted_list[right].original_index]`.
            *   If `current_sum < target`, increment `left` (need a larger sum).
            *   If `current_sum > target`, decrement `right` (need a smaller sum).
    *   **Time Complexity:** O(n log n) primarily due to the sorting step. The two-pointer scan itself is O(n).
    *   **Space Complexity:** O(n) to store the `(value, original_index)` pairs if a new list is created for sorting. Could be O(1) if modifying in-place (but this is usually not possible for this problem without losing original indices).
    *   **Trade-off:** This approach is very efficient for finding pairs in *already sorted* arrays, but the initial sorting step makes it generally slower than the hash map approach for this specific problem (O(n log n) vs O(n)). It's a valuable technique for problems where space is a critical constraint and an O(n log n) time complexity is acceptable, or when the input is naturally sorted.

---