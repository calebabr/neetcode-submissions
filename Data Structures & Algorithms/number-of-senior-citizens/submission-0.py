class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            print(s[13:15])
            if int(s[12:14]) > 60:
                count += 1
        return count