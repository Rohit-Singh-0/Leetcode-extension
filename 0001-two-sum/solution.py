class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        #time = O(n^2)
        #space = O(1)


        #Optimal solution - using hashmap
        # remainder_map = {}
        # for index, num in enumerate(nums):
        #     if num in remainder_map:
        #         return [index, remainder_map[num]]
        #     remainder_map[target-num] = index
        #time = O(n)
        #space = O(n)