"""
1.  Intersection of two arrays
Difficulty: Easy
Link:https://leetcode.com/problems/intersection-of-two-arrays

Time Complexity: O(N*M)
Space Complexity: O(N)
Pattern: Hash Table
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        set_nums2=set(nums2)
        for num in nums1:
            if num in nums2:
                result.append(num)
        all = list(set(result))
        return all