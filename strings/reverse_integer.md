# LeetCode 7 — Reverse Integer

## Problem

Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` makes the value go outside the signed 32-bit integer range:

```text
[-2^31, 2^31 - 1]
```

return `0`.

## Examples

```text
Input:  x = 123
Output: 321
```

```text
Input:  x = -123
Output: -321
```

```text
Input:  x = 120
Output: 21
```

## Idea

Convert the integer into a string, reverse the digits, and then convert it back into an integer.

There are three important cases:

1. If `x == 0`, return `0` directly.
2. If the number ends with `0`, remove the trailing zeroes first.
3. If the number is negative, keep the `-` sign at the front and only reverse the digits after it.

After reversing, check whether the result is still inside the 32-bit signed integer range.

## Python Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        string_x = str(x)

        if x == 0:
            return 0

        while string_x[(len(string_x) - 1)] == "0":
            string_x = string_x[0:(len(string_x) - 1)]

        output = ""
        
        if string_x[0:1] == "-":
            output = "-" + string_x[:0:-1]
        else:
            output = string_x[::-1]
        
        if int(output) < (-2**31) or int(output) > (2**31 - 1):
            return 0
        else:
            return int(output)
```

## Explanation

### Step 1: Convert integer to string

```python
string_x = str(x)
```

This makes it easier to reverse the digits using Python string slicing.

For example:

```python
x = 123
string_x = "123"
```

For a negative number:

```python
x = -123
string_x = "-123"
```

---

### Step 2: Handle zero

```python
if x == 0:
    return 0
```

If `x` is already `0`, reversing it is still `0`.

This also prevents problems later when checking the last character of the string.

---

### Step 3: Remove trailing zeroes

```python
while string_x[(len(string_x) - 1)] == "0":
    string_x = string_x[0:(len(string_x) - 1)]
```

If the number ends with `0`, those zeroes should disappear after reversing.

Example:

```python
x = 120
string_x = "120"
```

After removing the trailing zero:

```python
string_x = "12"
```

Then reversing gives:

```python
"21"
```

So the final result is:

```python
21
```

---

### Step 4: Reverse the number

```python
if string_x[0:1] == "-":
    output = "-" + string_x[:0:-1]
else:
    output = string_x[::-1]
```

#### Positive number

For a positive number, we can reverse the whole string:

```python
string_x = "123"
output = string_x[::-1]
```

Result:

```python
"321"
```

#### Negative number

For a negative number, we should not reverse the `-` sign.

Example:

```python
string_x = "-123"
```

This part:

```python
string_x[:0:-1]
```

means:

```text
Start from the end of the string and move backwards, but stop before index 0.
```

So:

```python
string_x[:0:-1]
```

returns:

```python
"321"
```

Then we add the negative sign back:

```python
output = "-" + "321"
```

Result:

```python
"-321"
```

---

### Step 5: Check 32-bit integer range

```python
if int(output) < (-2**31) or int(output) > (2**31 - 1):
    return 0
else:
    return int(output)
```

The valid range is:

```python
-2**31 <= output <= 2**31 - 1
```

Which is:

```text
-2147483648 to 2147483647
```

If the reversed number is outside this range, return `0`.

Otherwise, return the reversed integer.

## Walkthrough

### Example: `x = -120`

```python
string_x = str(-120)
```

So:

```python
string_x = "-120"
```

Remove trailing zero:

```python
string_x = "-12"
```

Since it starts with `-`:

```python
output = "-" + string_x[:0:-1]
```

`string_x[:0:-1]` gives:

```python
"21"
```

So:

```python
output = "-21"
```

Convert back to integer:

```python
return -21
```

## Complexity

Let `n` be the number of digits in `x`.

```text
Time Complexity:  O(n)
Space Complexity: O(n)
```

We use `O(n)` time because reversing the string takes time proportional to the number of digits.

We use `O(n)` space because the string version of the number is stored in memory.

## Note

This solution is very easy to understand because it uses strings. In some interviews, they may ask for a mathematical solution without converting the integer to a string.
