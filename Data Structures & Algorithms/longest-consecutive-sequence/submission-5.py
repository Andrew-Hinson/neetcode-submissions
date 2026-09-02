class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       # elements are not in order
       # O(n) time
       # one question, how to know where to start? What is lowest element?
       # I guess sorting the array is right out 
       # hash map the nums so that the func has some comprehension of what exists. only consider start if num -1 does NOT exist in given array. So iterate through array one time
        # set will get rid of dups out the gate
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # check if num is start of a sequence
            if num - 1 not in numSet:
                length = 1
                # check if num has a next num
                while num + length in numSet:
                    length += 1
                # compare length of the previous sequence 
                longest = max(length, longest)
        return longest
            

        