class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandAroundCenter ( s , left , right):
            while (left >= 0) and (right < len(s)) and ( s[left] == s[right]) : 
                left -= 1
                right += 1
            return s[left+1:right]
        
        longestSub = ""
        
        for i in range(len(s)):
            center = expandAroundCenter (s , i , i)
            inBetween = expandAroundCenter (s , i , i+1)
            longestSub = max (longestSub , center , inBetween , key = len)
            
        return longestSub
