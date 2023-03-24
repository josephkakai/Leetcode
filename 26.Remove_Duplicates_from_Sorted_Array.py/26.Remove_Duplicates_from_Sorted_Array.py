class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        l = len(nums)
        while i < l:
            if nums[i] in nums[:i]:
                del nums[i]
                l-=1
            else:
                i+=1
        return len(nums)
