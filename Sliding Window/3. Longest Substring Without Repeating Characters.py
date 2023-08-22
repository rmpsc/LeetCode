# MEDIUM
# Time: O(n) Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        pwwkew
           l
             r

        (k, e, w)

        res = 3
        '''
        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res