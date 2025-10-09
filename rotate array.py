
# rotate array 


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # handle cases when k > n
        nums[:] = nums[-k:] + nums[:-k]  # slice and rearrange
        
# Example usage:
solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]