class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        left, right = 0, 0
        longest = 1
        chars = set()
        while right < len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1
        return longest
        

        