"""
1.  Contains Duplicate
Difficulty: Easy
Link:https://leetcode.com/problems/contains-duplicate/

Time Complexity: O(N)
Space Complexity: O(N)
Pattern: Hash set
"""




class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        unique = set(nums)
        unique_length = len(unique)
        if unique_length < length :
            return True
        return False