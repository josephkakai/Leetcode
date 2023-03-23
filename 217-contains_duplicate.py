class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a seenvalue list
        seenValues = []

        # loop through nums list
        for num in nums:
            # check if the value in nums is in seenvalues
                if (num in seenValues):
                    return True
                # append seen values to the seevvalue variable    
                seenValues.append(num)
        return False
