class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        count = 1
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))
            print(count)
            count += 1
        return score