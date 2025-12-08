class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the intersection point in the cycle
        slow = fast = nums[0]
        while True:
            slow = nums[slow]    # move 1 step
            fast = nums[nums[fast]]  # move 2 steps
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow # or fast, both are at the duplicate



# 🧠 Intuition (Floyd’s Tortoise and Hare – Cycle Detection)

# This is the clever part.
# Think of the array as a linked list:
# Each index is a node

# From index i, you "go" to index nums[i]
# Since numbers are in [1..n] and we have n+1 numbers:

# Pigeonhole principle ⇒ must be a cycle
# The duplicate number is the entry point of the cycle

# We can use Floyd’s cycle-finding algorithm (same as “linked list cycle II”):

# Phase 1: Find intersection point
# Use two pointers:
# slow = nums[slow] (1 step)
# fast = nums[nums[fast]] (2 steps)

# Eventually they meet inside the cycle.

# Phase 2: Find cycle entry (duplicate number)
# Move one pointer to the start (slow = 0 or slow = nums[0] depending on implementation)
# Then move both pointers one step at a time:
# slow = nums[slow]
# fast = nums[fast]
# The point where they meet again is the duplicate number.
        





    
        # Phase 1: Find intersection

        # Start: slow = nums[0] = 1, fast = nums[0] = 1
        # Loop:
        # slow = nums[1] = 3
        # fast = nums[nums[1]] = nums[3] = 2
        # slow = nums[3] = 2
        # fast = nums[nums[2]] = nums[4] = 2
        # Now slow == fast == 2 → intersection found inside cycle.

        # Phase 2: Find cycle start (duplicate)
        # Reset slow = nums[0] = 1
        # Keep fast = 2

        # Now move both one step at a time:
        # slow = nums[1] = 3
        # fast = nums[2] = 4
        # slow = nums[3] = 2
        # fast = nums[4] = 2
        # They meet at value 2 → that’s the duplicate number ✅

        # ⏱️ Time & Space Complexity

        # Time: O(n) – both phase 1 and 2 are linear
        # Space: O(1) – just using a few variables