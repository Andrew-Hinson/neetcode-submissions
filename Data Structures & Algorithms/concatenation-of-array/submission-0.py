class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # array is "duplicated" into a new array
        # can i do this in O(n) by going through original array once
        # I could initialize the array to doulbe the length of the 1st array
        # then fill it.
        n = len(nums)
        ans = [0] * n * 2

        for i in range(len(nums)):
            
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        print(ans)
        return ans