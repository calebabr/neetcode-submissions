class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            print(s[12:14])
            if int(s[12:13]) > 60:
                count += 1
        return count