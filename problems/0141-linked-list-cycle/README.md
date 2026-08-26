<!-- LC-SYNC:AUTO-GENERATED:START — do not edit below, it is overwritten on every sync -->

# 141. Linked List Cycle

**Difficulty:** Easy  |  **LeetCode:** [linked-list-cycle](https://leetcode.com/problems/linked-list-cycle/)
**Topics:** Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm

**Latest submission:** ✅ Accepted in C — see [`solution.c`](solution.c)

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true`* if there is a cycle in the linked list*. Otherwise, return `false`.

 

**Example 1:**

*[image omitted — view on LeetCode]*

```

**Input:** head = [3,2,0,-4], pos = 1
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

```

**Example 2:**

*[image omitted — view on LeetCode]*

```

**Input:** head = [1,2], pos = 0
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

```

**Example 3:**

*[image omitted — view on LeetCode]*

```

**Input:** head = [1], pos = -1
**Output:** false
**Explanation:** There is no cycle in the linked list.

```

 

**Constraints:**

- The number of the nodes in the list is in the range `[0, 10^4]`.

- `-10^5 <= Node.val <= 10^5`

- `pos` is `-1` or a **valid index** in the linked-list.

 

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## Submission History

| Date | Status | Language | Runtime | Memory | Code |
| --- | --- | --- | --- | --- | --- |
| 2026-08-26 10:31 UTC | ✅ Accepted | C | 14 ms | 12 MB | [view](submissions/1787740298_Accepted_2120679018.c) |
| 2026-08-26 10:16 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787739378_Wrong-Answer_2120665591.c) |
| 2026-08-26 10:00 UTC | ⏱️ Time Limit Exceeded | C | N/A | N/A | [view](submissions/1787738439_Time-Limit-Exceeded_2120651176.c) |

<!-- LC-SYNC:AUTO-GENERATED:END -->

<!-- LC-SYNC:PERSONAL:START — write freely below, this section is never touched by sync -->

# My approach - NA
<!-- LC-SYNC:PERSONAL:END -->
