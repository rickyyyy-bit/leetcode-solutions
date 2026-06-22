# 3. Longest Substring Without Repeating Characters

## Problem

Given a string `s`, return the length of the longest substring without repeating characters.

A substring must be continuous.

## Examples

### Example 1

```text
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.
```

### Example 2

```text
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with length 1.
```

### Example 3

```text
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3.
```

## Approach: Sliding Window

We keep a window of characters with no duplicates.

Use two pointers:

- `left`: start of the current substring window
- `right`: current character position while scanning the string

We also keep a dictionary called `last_seen`, where:

```python
last_seen[char] = latest index where char appeared
```

When we see a repeated character that is still inside the current window, we move `left` to the position after the previous occurrence.

## Step-by-step idea

For `s = "pwwkew"`:

```text
p       -> length 1
pw      -> length 2
pww     -> repeat w, move left
w       -> length 1
wk      -> length 2
wke     -> length 3
ew      -> length 2
```

The longest substring without repeating characters is `"wke"`, so the answer is `3`.

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
```

## Complexity

```text
Time Complexity: O(n)
Space Complexity: O(min(n, charset size))
```

Each character is visited once, and the dictionary stores the characters currently or previously seen.

## Notes

My first idea was to keep building a string called `longest` and check whether the current character already exists in it. That works logically, but checking membership and using `index()` on strings can make the solution slower.

The sliding window with a dictionary is cleaner and faster for large inputs.
