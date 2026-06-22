class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        count = 0
        largestN = 0
        for i in range(len(s)):
            if s[i] in longest:
                longest = longest[longest.index(s[i]) + 1:] + s[i]
                if largestN <= count:
                    largestN = count
                count = len(longest)
            else:
                count += 1
                longest += s[i]
        if largestN <= count:
            largestN = count
        return largestN