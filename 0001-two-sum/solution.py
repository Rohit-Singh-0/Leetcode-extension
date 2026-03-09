class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Optimal solution - using hashmap
        remainder_map = {}
        for index, num in enumerate(nums):
            if num in remainder_map:
                return [index, remainder_map[num]]
            remainder_map[target-num] = index
        #time = O(n)
        #space = O(n)