class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        end = 0

        def expand_from_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # After the loop, left and right are one step too far
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindrome, e.g. "aba"
            left1, right1 = expand_from_center(i, i)

            # Even length palindrome, e.g. "bb"
            left2, right2 = expand_from_center(i, i + 1)

            if right1 - left1 > end - start:
                start = left1
                end = right1

            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]

