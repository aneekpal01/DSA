class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()

        left = 0
        max_len = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            current_length = right - left + 1
            max_len = max(max_len, current_length)

        return max_len