# LeetCode 9 - Palindrome Number

## Problem

Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

A palindrome number reads the same from left to right and from right to left.

For example:

```text
121
```

is a palindrome because it is still `121` when reversed.

But:

```text
-121
```

is not a palindrome because from right to left it becomes:

```text
121-
```

---

## My Solution

```python
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)
        len_x = len(str_x) - 1
        count = math.ceil(len_x / 2) - 1

        while count >= 0:
            if str_x[0 + count] != str_x[len_x - count]:
                return False
            count -= 1

        return True
```

---

## Important Note

My code uses:

```python
math.ceil()
```

So I need to include:

```python
import math
```

at the top of the file.

Without this import, Python will give an error:

```text
NameError: name 'math' is not defined
```

---

## Main Idea

The idea is to compare characters from the left side and the right side.

For example:

```python
x = 121
```

After converting it to a string:

```python
str_x = "121"
```

We compare:

```text
left side       right side
   1       ==      1
```

If every pair matches, then it is a palindrome.

If one pair is different, then it is not a palindrome.

---

## Step-by-Step Explanation

### Step 1: Negative numbers are not palindromes

```python
if x < 0:
    return False
```

If the number is negative, we immediately return `False`.

Example:

```python
x = -121
```

From left to right, it reads:

```text
-121
```

From right to left, it becomes:

```text
121-
```

These are not the same, so negative numbers are not palindromes.

---

### Step 2: Convert the number to a string

```python
str_x = str(x)
```

This allows us to check each digit like a character.

Example:

```python
x = 121
str_x = "121"
```

Now we can use indexes:

```text
index:  0 1 2
value:  1 2 1
```

---

### Step 3: Store the last index

```python
len_x = len(str_x) - 1
```

This stores the last index of the string.

For example:

```python
str_x = "121"
```

The length is:

```python
len(str_x) = 3
```

So:

```python
len_x = 3 - 1
len_x = 2
```

That means the last character is:

```python
str_x[2]
```

---

### Step 4: Decide how many comparisons are needed

```python
count = math.ceil(len_x / 2) - 1
```

The goal is to only compare half of the string.

For example:

```python
str_x = "121"
```

The last index is:

```python
len_x = 2
```

So:

```python
count = math.ceil(2 / 2) - 1
count = math.ceil(1) - 1
count = 1 - 1
count = 0
```

So we only need one comparison:

```python
str_x[0] == str_x[2]
```

That means:

```python
"1" == "1"
```

---

## Example 1: `x = 121`

Input:

```python
x = 121
```

Convert to string:

```python
str_x = "121"
```

Last index:

```python
len_x = len("121") - 1
len_x = 3 - 1
len_x = 2
```

Initial count:

```python
count = math.ceil(2 / 2) - 1
count = 0
```

Now enter the loop:

```python
while count >= 0:
```

Since `count = 0`, the loop runs.

Compare:

```python
str_x[0 + count] != str_x[len_x - count]
```

Substitute the values:

```python
str_x[0 + 0] != str_x[2 - 0]
```

So:

```python
str_x[0] != str_x[2]
```

That means:

```python
"1" != "1"
```

This is `False`, so we do not return `False`.

Then:

```python
count -= 1
```

So:

```python
count = -1
```

The loop stops.

Return:

```python
True
```

Final output:

```python
True
```

---

## Example 2: `x = 123`

Input:

```python
x = 123
```

Convert to string:

```python
str_x = "123"
```

Last index:

```python
len_x = 2
```

Initial count:

```python
count = 0
```

Compare:

```python
str_x[0] != str_x[2]
```

That means:

```python
"1" != "3"
```

This is `True`.

So we immediately return:

```python
False
```

Final output:

```python
False
```

---

## Example 3: `x = 1221`

Input:

```python
x = 1221
```

Convert to string:

```python
str_x = "1221"
```

Indexes:

```text
index:  0 1 2 3
value:  1 2 2 1
```

Last index:

```python
len_x = 3
```

Initial count:

```python
count = math.ceil(3 / 2) - 1
count = math.ceil(1.5) - 1
count = 2 - 1
count = 1
```

### First comparison

```python
count = 1
```

Compare:

```python
str_x[0 + 1] != str_x[3 - 1]
```

So:

```python
str_x[1] != str_x[2]
```

That means:

```python
"2" != "2"
```

They are the same, so continue.

Then:

```python
count -= 1
```

Now:

```python
count = 0
```

### Second comparison

Compare:

```python
str_x[0 + 0] != str_x[3 - 0]
```

So:

```python
str_x[0] != str_x[3]
```

That means:

```python
"1" != "1"
```

They are the same, so continue.

Then:

```python
count -= 1
```

Now:

```python
count = -1
```

The loop stops.

Return:

```python
True
```

Final output:

```python
True
```

---

## Why This Works

The code checks whether the left-side digit matches the right-side digit.

This part checks the pair:

```python
str_x[0 + count] != str_x[len_x - count]
```

The left index is:

```python
0 + count
```

The right index is:

```python
len_x - count
```

If the two characters are different, then the number cannot be a palindrome.

So we return:

```python
False
```

If all checked pairs match, we return:

```python
True
```

---

## Complexity

Let `n` be the number of digits in `x`.

### Time Complexity

```text
O(n)
```

The code checks about half of the digits, but in Big-O notation this is still `O(n)`.

### Space Complexity

```text
O(n)
```

The code converts the integer into a string, so it uses extra space for the string.
