#Duplicate Integer
#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

#bruit force 

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# Create an instance of the Solution class
solution = Solution()

# Sample input
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

# Call the method and print the result
print(solution.hasDuplicate(nums))  # Output should be True
