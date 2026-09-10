class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ok I swear I've done this before but that doesnt matter now
        # this is a sliding window problem
        #return the LENGTH of the longest substring, which contains ONLY ONE DISTINCT character
        # so if string is "XYYX" and k=2, then I could replace Y's with X's and have "XXXX", meaning answer would be 4. OR "YYYY" = 4.
        #ex 2; "AAABABB", k=1, output 5, because "AAAAA".
        # sliding window key alg, r - l + 1
        # for this prob, l = 0, r = 1
        # iterate r compare to l
        # if s[r] encounters dif element of s[l] and under k
        # create total var that is the sort alg, r - l +1 and holds that val
        # compare to last total with max()

        count = {}
        l = 0
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])

            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res