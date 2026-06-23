# 5. Longest Palindromic Substring

## Problem

Given a string `s`, return the **longest palindromic substring** in `s`.

A **palindrome** is a string that reads the same forwards and backwards.

A **substring** means the characters must be continuous.

---

## Examples

### Example 1

```text
Input: s = "babad"
Output: "bab"
```

`"aba"` is also a valid answer.

### Example 2

```text
Input: s = "cbbd"
Output: "bb"
```

---

## Key Idea

Every palindrome has a **center**.

There are two possible types of centers:

### 1. Odd-length palindrome

Example:

```text
aba
 ^
```

The center is one character.

### 2. Even-length palindrome

Example:

```text
bb
^^
```

The center is between two characters.

So for every index `i`, we try to expand around:

```python
(i, i)      # odd length palindrome
(i, i + 1)  # even length palindrome
```

While the left and right characters are the same, we keep expanding.

---

## Walkthrough

For:

```text
s = "babad"
```

At index `1`, the character is `"a"`.

```text
b a b a d
  ^
```

Expand left and right:

```text
b a b
```

This gives `"bab"`.

At index `2`, the character is `"b"`.

```text
b a b a d
    ^
```

Expand left and right:

```text
a b a
```

This gives `"aba"`.

Both `"bab"` and `"aba"` have length `3`, so either answer is accepted.

---

## Python Solution

```python
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

            # After the loop, left and right are one step outside the palindrome
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindrome, e.g. "aba"
            left1, right1 = expand_from_center(i, i)

            # Even-length palindrome, e.g. "bb"
            left2, right2 = expand_from_center(i, i + 1)

            if right1 - left1 > end - start:
                start = left1
                end = right1

            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]
```

---

## Why `left + 1` and `right - 1`?

Inside the loop, we keep expanding while the characters match.

When the loop stops, it means one of these happened:

1. `left` went out of bounds
2. `right` went out of bounds
3. `s[left] != s[right]`

So `left` and `right` are no longer pointing to valid palindrome positions.

That is why we return:

```python
left + 1, right - 1
```

---

## Complexity

Let `n` be the length of the string.

For each index, we may expand across the string.

### Time Complexity

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

We only store a few variables, so no extra large data structure is needed.

---

## Summary

The main idea is:

1. Treat every character as a possible palindrome center.
2. Check both odd and even length palindromes.
3. Expand outward while both sides match.
4. Keep track of the longest palindrome found.

This is a clean and standard solution for LeetCode 5.
