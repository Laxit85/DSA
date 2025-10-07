# Two sum 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
# Output: [0, 1]