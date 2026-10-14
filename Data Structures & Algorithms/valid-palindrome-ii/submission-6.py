class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Normal Palindrome check
        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        # Run palindrome check but if we find a mismatch, "delete" l or r and see which one returns valid. We can only delete once.
        while l < r:
            if s[l] != s[r]:
                return (palindrome(l + 1, r) or palindrome(l, r - 1))
            l += 1
            r -= 1
        return True