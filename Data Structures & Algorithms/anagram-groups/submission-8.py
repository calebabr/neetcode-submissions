class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tList = {} # Mapping freq to lists
        d = defaultdict(list)
        for word in strs:
            alpha = [0] * 26
            for i in word:
                num = ord(i) - ord('a')
                alpha[num] += 1
            alpha = tuple(alpha)
            d[alpha].append(word)
        return list(d.values())