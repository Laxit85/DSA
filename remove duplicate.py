class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0  # pointer for last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # move unique element forward

        return i + 1  # length of unique elements

# Example usage:
solution = Solution()
nums = [1, 1, 2]
length = solution.removeDuplicates(nums)
print(length)  # Output: 2
print(nums[:length])  # Output: [1, 2]