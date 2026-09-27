"""
1.  Longest Common Prefix
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix

Time Complexity: O(n*m)
Space Complexity: O(m)
Pattern: Vertical Scanning

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        
        
        for amount in range(len(strs[0])+1):
            prefix = strs[0][:amount]
            for word in range(1, len(strs)):
                if prefix != strs[word][:amount]:
                    return strs[0][:amount-1]
        return prefix
            
            
        
            
                
                    
                
            