class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        i = 0
        while (i < l):
            if nums[i] == val:
                del nums[i]
                l-=1
            else:
                i+=1
        return l   
