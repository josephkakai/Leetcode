class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we check if nums has value if not it exits 
        if (nums is None):
            return
        
        """ we declare two variables and assign to the\
         first element in the list """
        currentSum = nums[0]
        maxSum = nums[0]

        # we loop through nums starting from the second element
        for num in nums[1:]:
            # we keep track of the current sum by assigning the largest sum
            currentSum = max(num, currentSum + num)
            # now we store the largest subarray to the maxsumn variable
            maxSum = max(maxSum, currentSum)
        # And then we return the max subarray
        return maxSum
