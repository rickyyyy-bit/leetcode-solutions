# LeetCode 6 - Zigzag Conversion

## Problem

Given a string `s` and an integer `numRows`, write the string in a zigzag pattern with `numRows` rows, then read the pattern row by row.

Example:

```text
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

The zigzag pattern looks like this:

```text
P   A   H   N
A P L S I I G
Y   I   R
```

Reading row by row gives:

```text
PAHNAPLSIIGYIR
```

---

## Idea

Instead of actually drawing the zigzag shape, we can store characters directly into different rows.

We move through the rows like this:

```text
0 → 1 → 2 → 1 → 0 → 1 → 2 → 1 → ...
```

For `numRows = 3`, the row movement goes down until the bottom row, then goes back up to the top row.

So we need:

* `rows`: a list storing the characters for each row
* `curr_row`: the row we are currently adding a character to
* `direction`: tells us whether we are moving down or up

When we reach the top row, we start moving down.

When we reach the bottom row, we start moving up.

---

## Python Solution

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = 1

        for ch in s:
            rows[curr_row] += ch

            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        return "".join(rows)
```

---

## Explanation

First, we handle edge cases:

```python
if numRows == 1 or numRows >= len(s):
    return s
```

If there is only one row, there is no zigzag, so we return the original string.

If `numRows` is greater than or equal to the length of the string, the string also does not need to change.

Then we create an empty string for each row:

```python
rows = [""] * numRows
```

For example, if `numRows = 3`, then:

```python
rows = ["", "", ""]
```

We then keep track of the current row and direction:

```python
curr_row = 0
direction = 1
```

`direction = 1` means we are moving down.

`direction = -1` means we are moving up.

For every character in the string:

```python
for ch in s:
    rows[curr_row] += ch
```

We put the character into the current row.

Then we check whether we need to change direction:

```python
if curr_row == 0:
    direction = 1
elif curr_row == numRows - 1:
    direction = -1
```

If we are at the top row, we go down.

If we are at the bottom row, we go up.

Finally, we move to the next row:

```python
curr_row += direction
```

At the end, all rows are joined together:

```python
return "".join(rows)
```

---

## Example Walkthrough

For:

```python
s = "PAYPALISHIRING"
numRows = 3
```

The characters go into rows like this:

```text
P goes to row 0
A goes to row 1
Y goes to row 2
P goes to row 1
A goes to row 0
L goes to row 1
I goes to row 2
S goes to row 1
H goes to row 0
I goes to row 1
R goes to row 2
I goes to row 1
N goes to row 0
G goes to row 1
```

So the rows become:

```python
rows = ["PAHN", "APLSIIG", "YIR"]
```

Joining them gives:

```python
"PAHNAPLSIIGYIR"
```

---

## Complexity

Let `n` be the length of the string.

Time complexity:

```text
O(n)
```

We visit every character once.

Space complexity:

```text
O(n)
```

We store all characters in the row list before joining them.
