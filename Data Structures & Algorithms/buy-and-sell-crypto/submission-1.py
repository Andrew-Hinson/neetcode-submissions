class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # i know they say this is a sliding window problem
    # so basically im looking at the difference between the smaller number on the left and larger num on the right, kind of like the water container problem.
    # i.e. I start one pointer on the left, one on the right, for the one on the left, I increment it if the next number is lower than the previous. For the right number I decrement it if the next num is more than the left num AND greater than the num its on. 
    # for example lets say this fake array exists
    # [10,8,4,7,9,3,2]
    # my left pointer increments as long as next num is lower than current num, I end up at 4
    # my right pointer decrements as long as next num is greater than current num AND is greater than left. 
    # I then calculate the difference and return.
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP