"""
1.  Single Number
Difficulty: Easy
Link:https://leetcode.com/problems/single-number/

Time Complexity: O(N)
Space Complexity: O(N)
Pattern: Hash Map
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        pairs={}

        for num in nums: 
            if num in pairs:
                pairs[num] +=1
            else:
                pairs[num] = 1
        for num, count in pairs.items():
            if count == 1:
                return num

