class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        # no duplicate triplets, 2 pointer solution
        # 3 sum. So 3 pointers maybe?

        # brute force, for each num, iterate through array and find values that satisfy equation. 
        # maybe hashmap would work, items dont need to be next to each other. 
        # dont need the array position of the item. 
        # iterate over array, add everything to hash map
        # hashmap has the key = value, value = freq. doesnt matter could be other way around
        # I then start with one value. I see if any 2 other nums in the map will satisfy the equation. If not, move to next num. I also check if freq of num will help solve equation. I then add that triplet to the output. If nothing found, I output an empty array
        # so first I assign one pointer to first value as [i] I check freq of num to see if combo exists as my next value [j], like 2, 1s. I then check for third value [k] like -2. If doesnt exist, I use one 1. I then use the next avail value as my [j].
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return output
                
                

            
            
