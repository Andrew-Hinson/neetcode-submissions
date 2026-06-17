class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #the cheap and easy method, returns true if they are equal
        #return sorted(s) == sorted(t)

        #understanding the problem 
        #hashmaps are good here to count frequency of characters 
        #check length first to rule out easy comparisons
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True