"""
1.  Majority Element
Difficulty: Easy
Link:https://leetcode.com/problems/majority-element

Time Complexity: O(N log N)
Space Complexity: O(N)
Pattern: Sorted
"""



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        end=sorted(nums)
        length=len(nums)

        return end[length//2]