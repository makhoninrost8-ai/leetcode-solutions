"""
1.  PascalsTriangle
Difficulty: Easy
Link:https://leetcode.com/problems/pascals-triangle

Time Complexity: O(N)
Space Complexity: O(1)
Pattern: One Pass
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            elif price - min_price>max_profit:
                max_profit=price - min_price
        return max_profit