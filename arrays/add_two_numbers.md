# 2. Add Two Numbers

**Difficulty:** Medium
**Topic:** Linked List, Math
**LeetCode:** https://leetcode.com/problems/add-two-numbers/

## Problem

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each node contains one digit.

Add the two numbers and return the result as a linked list.

## Example

```text
Input:
l1 = 2 -> 4 -> 3
l2 = 5 -> 6 -> 4

Output:
7 -> 0 -> 8
```

Explanation:

```text
342 + 465 = 807
```

Because the digits are stored in reverse order:

```text
2 -> 4 -> 3 means 342
5 -> 6 -> 4 means 465
7 -> 0 -> 8 means 807
```

## Approach

Use a dummy node to build the result linked list.

We go through `l1` and `l2` at the same time.

For each step:

1. Get the current value from `l1`.
2. Get the current value from `l2`.
3. Add both values and the carry.
4. The result digit is `total % 10`.
5. The new carry is `total // 10`.
6. Add the digit as a new node to the result list.

The loop continues while there is still a node in `l1`, a node in `l2`, or a remaining carry.

## Python Solution

```python
from typing import Optional

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
```

## Key Idea

```python
dummy = ListNode(0)
curr = dummy
```

`dummy` is a fake starting node.

`curr` is used to build the answer list.

When we add a new node:

```python
curr.next = ListNode(digit)
curr = curr.next
```

The first line attaches the new node.

The second line moves `curr` forward.

At the end, we return:

```python
return dummy.next
```

because `dummy` itself is not part of the real answer.

## Complexity

**Time Complexity:** `O(max(m, n))`

Where `m` and `n` are the lengths of the two linked lists.

**Space Complexity:** `O(max(m, n))`

The result linked list stores the answer.
