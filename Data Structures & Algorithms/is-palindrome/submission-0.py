class Solution:
    def isPalindrome(self, s: str) -> bool:
       # two pointer solution
       # one pointer at beginning, one at end
       # do I .join() to get rid of white space? 
       # for c in s, is s[left] == s[right]? left +=1 right -=1
       # iterate through string as long as left pointer is not greater than right
        # dont want to import anything, i could ignore white space
        # I have to ignore punctuation if exists
        
        j = "".join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(j) - 1
        print (j)
        for c in j:
            if left <= right:
                if j[left] != j[right]:
                    return False

            left += 1
            right -= 1
        return True