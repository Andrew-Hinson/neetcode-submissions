class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # iterate through string
       # add characters to hashmap with r pointer
       # if char exists, shrink the window with l pointer and remove
       # chars from hash set that are that are excluded from the window as l pointer moves. So s[l] is removed from hash set
       # each iteration, update result with length of current window
       # r - l + 1 if greater than last current result
       # return max result

# "zxyzxyz"
# output: 3

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
