class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        AXBAY
          l
            r
        k = 2

        {A:1, X:0, B:1, Y:1}
        res = 4
        '''
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        
        return res