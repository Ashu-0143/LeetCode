<!-- LC-SYNC:AUTO-GENERATED:START — do not edit below, it is overwritten on every sync -->

# 202. Happy Number

**Difficulty:** Easy  |  **LeetCode:** [happy-number](https://leetcode.com/problems/happy-number/)
**Topics:** Hash Table, Math, Two Pointers, Floyd's Cycle Finding Algorithm

**Latest submission:** ✅ Accepted in C — see [`solution.c`](solution.c)

## Problem Statement

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.

- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.

- Those numbers for which this process **ends in 1** are happy.

Return `true` *if* `n` *is a happy number, and* `false` *if not*.

 

**Example 1:**

```

**Input:** n = 19
**Output:** true
**Explanation:**
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

```

**Example 2:**

```

**Input:** n = 2
**Output:** false

```

 

**Constraints:**

- `1 <= n <= 2^31 - 1`

## Submission History

| Date | Status | Language | Runtime | Memory | Code |
| --- | --- | --- | --- | --- | --- |
| 2026-08-23 10:20 UTC | ✅ Accepted | C | 0 ms | 8.5 MB | [view](submissions/1787480442_Accepted_2117209557.c) |
| 2026-08-23 10:19 UTC | ✅ Accepted | C | 76 ms | 8.5 MB | [view](submissions/1787480362_Accepted_2117208322.c) |
| 2026-08-23 09:44 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787478250_Wrong-Answer_2117177305.c) |
| 2026-08-23 09:42 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787478165_Wrong-Answer_2117176062.c) |
| 2026-08-23 04:30 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787459406_Wrong-Answer_2116905976.c) |
| 2026-08-23 04:28 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787459317_Wrong-Answer_2116904933.c) |

<!-- LC-SYNC:AUTO-GENERATED:END -->

<!-- LC-SYNC:PERSONAL:START — write freely below, this section is never touched by sync -->

### My Approach

_How I personally solved it — write this yourself._

### Complexity

- Time complexity:
- Space complexity:

### My Notes

_Mistakes made, edge cases missed, anything worth remembering._

### What I Learned

_Anything useful for next time._

<!-- LC-SYNC:PERSONAL:END -->
