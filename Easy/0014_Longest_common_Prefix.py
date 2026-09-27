"""
1.  Longest Common Prefix
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix

Time Complexity: O(n*m^2)
Space Complexity: O(m)
Pattern: Vertical Scanning

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        ammount=0
        
        for ammount in range(len(strs[0])+1):
            prefix = strs[0][:ammount]
            for word in range(1, len(strs)):
                if prefix != strs[word][:ammount]:
                    return strs[0][:ammount-1]
        return prefix
            
            
        
            
                
                    
                
            