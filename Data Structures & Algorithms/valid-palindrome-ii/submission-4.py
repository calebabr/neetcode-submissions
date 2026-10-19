class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        deletedOne = False
        while l <= r:
            if s[l] != s[r]: # Delete at either l or r
                if s[l] == s[r - 1] and not deletedOne: # "delete" at r
                    r -= 1
                    deletedOne = True
                elif s[l + 1] == s[r] and not deletedOne: # "delete" at l
                    l += 1
                    deletedOne = True
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True