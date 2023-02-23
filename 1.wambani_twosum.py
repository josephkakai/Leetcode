class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_dict = {}

        """iterate throigh input list"""
        for i, num in enumerate(nums):
            if target - num in new_dict:
                """if yes return two indices"""
                return [new_dict[target - num], i]
            """otherwise add the lement to dict"""
            new_dict[num] = i
