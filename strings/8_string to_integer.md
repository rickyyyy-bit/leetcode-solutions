# LeetCode 8 - String to Integer (atoi)

## Problem

We need to implement the function:

```python
myAtoi(s: str) -> int
```

The function converts a string into a 32-bit signed integer.

The valid 32-bit signed integer range is:

```text
[-2^31, 2^31 - 1]
```

Which is:

```text
[-2147483648, 2147483647]
```

If the result is smaller than `-2147483648`, return `-2147483648`.

If the result is larger than `2147483647`, return `2147483647`.

---

## Main Idea

We do not need many complicated `if else` statements.

We can solve the problem in 4 clear steps:

1. Skip leading spaces.
2. Check whether there is a `+` or `-` sign.
3. Read digits one by one.
4. Clamp the final answer into the 32-bit integer range.

---

## Python Solution

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        # 1. Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1

        # 3. Read digits
        result = 0

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # 4. Clamp result to 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN

        if result > INT_MAX:
            return INT_MAX

        return result
```

---

## Step-by-Step Explanation

### Step 1: Skip leading spaces

Example:

```python
s = "   -42"
```

At the beginning, there are spaces.

We move the pointer `i` forward until we reach the first non-space character.

```text
"   -42"
    ^
```

Now `i` points to `"-"`.

---

### Step 2: Check the sign

If the current character is `"-"`, the number is negative.

```python
sign = -1
```

If the current character is `"+"`, the number is positive.

```python
sign = 1
```

If there is no sign, we also assume the number is positive.

```python
sign = 1
```

Example:

```python
s = "-42"
```

We see `"-"`, so:

```python
sign = -1
```

Then we move `i` to the next character.

```text
"-42"
  ^
```

Now `i` points to `"4"`.

---

### Step 3: Read digits

This line is the most important part:

```python
result = result * 10 + int(s[i])
```

For example, if we are reading `"123"`:

```text
start:
result = 0

read '1':
result = 0 * 10 + 1 = 1

read '2':
result = 1 * 10 + 2 = 12

read '3':
result = 12 * 10 + 3 = 123
```

So the string `"123"` becomes the integer `123`.

We keep reading while the current character is a digit.

When we meet a non-digit character, we stop.

---

## Important Example: `"0-1"`

Input:

```python
s = "0-1"
```

Output:

```python
0
```

This is because `"0-1"` is a string, not the math expression `0 - 1`.

The function reads the string from left to right.

### Step 1: Skip whitespace

There is no leading whitespace.

```text
"0-1"
 ^
```

The pointer is at `"0"`.

### Step 2: Check sign

The current character is `"0"`.

It is not `"-"` or `"+"`.

So the sign stays positive.

```python
sign = 1
```

### Step 3: Read digits

The current character `"0"` is a digit.

So we read it:

```python
result = 0
```

Then we move to the next character.

```text
"0-1"
  ^
```

Now the current character is `"-"`.

`"-"` is not a digit, so we stop reading.

We do not read the `"1"`.

### Final result

```python
result = 0
sign = 1
```

So:

```python
0 * 1 = 0
```

Final output:

```python
0
```

---

## More Examples

### Example 1

Input:

```python
s = "42"
```

Output:

```python
42
```

Explanation:

There are no spaces and no sign.

We read `"42"` directly.

---

### Example 2

Input:

```python
s = "   -42"
```

Output:

```python
-42
```

Explanation:

We skip spaces, see `"-"`, then read `"42"`.

The final result is:

```python
42 * -1 = -42
```

---

### Example 3

Input:

```python
s = "4193 with words"
```

Output:

```python
4193
```

Explanation:

We read digits until we reach a non-digit character.

```text
"4193 with words"
     ^
```

The space after `3` is not a digit, so we stop.

---

### Example 4

Input:

```python
s = "words and 987"
```

Output:

```python
0
```

Explanation:

The first character is `"w"`.

It is not a space, sign, or digit.

So no number can be read.

Return `0`.

---

### Example 5

Input:

```python
s = "-91283472332"
```

Output:

```python
-2147483648
```

Explanation:

The number is smaller than the minimum 32-bit signed integer.

So we clamp it to:

```python
-2147483648
```

---

## Why This Does Not Need Many `if else`

The problem looks complicated, but it is really just pointer movement.

We only need:

- A `while` loop to skip spaces.
- A small `if / elif` to check the sign.
- A `while` loop to read digits.
- Two `if` checks to clamp the final answer.

The main logic is simple:

```python
while i < n and s[i].isdigit():
    result = result * 10 + int(s[i])
    i += 1
```

This builds the number digit by digit.

---

## Complexity

Let `n` be the length of the string.

### Time Complexity

```text
O(n)
```

We scan the string at most once.

### Space Complexity

```text
O(1)
```

We only use a few variables.
