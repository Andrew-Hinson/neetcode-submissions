class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       #each answer is a product of array as its iterated through. so for each num, multiply everything else together and output it.
       #strategy, this sounds like classic prefix array type solution.
       #I want to iterate through this array once.

    #n = len(nums)
    #prefix = [1] * (n + 1)

        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
