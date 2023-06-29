class Solution:
    def findDuplicate(self, nums) -> int:
        nums.sort

        low = 0
        high = len(nums) - 1
        res = 0

        while (low <= high):
            mid = low + (high - low) // 2

            if nums[mid] > mid:
                low = mid + 1
            else:
                res = nums[mid]
                high = mid - 1
        return res
