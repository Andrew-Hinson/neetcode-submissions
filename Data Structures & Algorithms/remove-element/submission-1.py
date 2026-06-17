class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
# remove in place
# return k
# removing all items = val
# iterate through once
# two pointers
# we swap the array in place except for the val we dont want
        k = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[k] = nums[r]
            # swapping in place if doesn't = the val
                k += 1
        return k