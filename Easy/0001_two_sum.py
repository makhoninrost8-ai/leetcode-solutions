"""
1.  Two Sum
Difficulty: Easy
Link:https://leetcode.com/problems/two-sum

Time Complexity: O(N)
Space Complexity: O(N)
Pattern: Hash Map
"""



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i, num in enumerate(nums):
            need=target-num

            if need in seen:
                return[seen[need], i]
            
            seen[num] = i 
