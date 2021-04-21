class Solution(object):
    def lengthOfLongestSubstring(self, s):  
        # set to check for duplicates
        s_set = set()
        # two pointers
        first, second = 0, 0
        # tracks longest length and temp longest length
        max, temp = 0, 0

        # runs until there's no more letters to check
        while first < len(s):
            if s[second] in s_set:
                if temp > max:
                    max = temp
                # reset for next letter
                temp = 0
                first += 1
                second = first
                s_set.clear()
            else:
                s_set.add(s[second])
                temp += 1
                # if statement in case second goes out of range
                if second + 1 < len(s):
                    second += 1

        return max
