import random

class Solution:
    def is_sorted(self, data):
        """Check if the list is sorted in-place."""
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                return False
        return True

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while not self.is_sorted(nums):
            random.shuffle(nums)  # Modifies data in-place
    
        