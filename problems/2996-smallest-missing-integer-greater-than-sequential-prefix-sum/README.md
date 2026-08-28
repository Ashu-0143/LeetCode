<!-- LC-SYNC:AUTO-GENERATED:START — do not edit below, it is overwritten on every sync -->

# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

**Difficulty:** Easy  |  **LeetCode:** [smallest-missing-integer-greater-than-sequential-prefix-sum](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/)
**Topics:** Array, Hash Table, Sorting

**Latest submission:** ✅ Accepted in C — see [`solution.c`](solution.c)

## Problem Statement

You are given a **0-indexed** array of integers `nums`.

A prefix `nums[0..i]` is **sequential** if, for all `1 <= j <= i`, `nums[j] = nums[j - 1] + 1`. In particular, the prefix consisting only of `nums[0]` is **sequential**.

Return *the **smallest** integer* `x` *missing from* `nums` *such that* `x` *is greater than or equal to the sum of the **longest** sequential prefix.*

 

**Example 1:**

```

**Input:** nums = [1,2,3,2,5]
**Output:** 6
**Explanation:** The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

```

**Example 2:**

```

**Input:** nums = [3,4,5,1,12,14,13]
**Output:** 15
**Explanation:** The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

```

 

**Constraints:**

- `1 <= nums.length <= 50`

- `1 <= nums[i] <= 50`

## Submission History

| Date | Status | Language | Runtime | Memory | Code |
| --- | --- | --- | --- | --- | --- |
| 2026-08-28 10:15 UTC | ✅ Accepted | C | 0 ms | 10.6 MB | [view](submissions/1787912138_Accepted_2122774846.c) |
| 2026-08-28 10:15 UTC | ✅ Accepted | C | 2 ms | 10.6 MB | [view](submissions/1787912110_Accepted_2122774507.c) |
| 2026-08-28 10:09 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787911774_Wrong-Answer_2122770394.c) |
| 2026-08-28 10:06 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787911591_Wrong-Answer_2122768098.c) |
| 2026-08-28 10:04 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787911453_Wrong-Answer_2122766322.c) |
| 2026-08-28 07:29 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787902151_Wrong-Answer_2122660736.c) |
| 2026-08-28 07:26 UTC | ❌ Wrong Answer | C | N/A | N/A | [view](submissions/1787901961_Wrong-Answer_2122658642.c) |
| 2026-08-28 07:23 UTC | 💥 Runtime Error | C | N/A | N/A | [view](submissions/1787901819_Runtime-Error_2122657068.c) |

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
