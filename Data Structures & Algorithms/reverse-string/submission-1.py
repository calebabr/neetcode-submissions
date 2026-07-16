class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = ""
        st = 0
        en = len(s) - 1
        while st < en:
            tmp = s[st]
            s[st] = s[en]
            s[en] = tmp
            st += 1
            en -= 1
             