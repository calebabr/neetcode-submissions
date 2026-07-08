class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        d = defaultdict(list)
        totalList = list()
        for word in strs: # convert list of words to dict of words to freq list
            alpha = [0] * 26
            for i in word:
                letterNum = ord(i) - 97 
                alpha[letterNum] += 1
            alpha = tuple(alpha)
            # counter[word] = alpha
            d[alpha].append(word)
            # print(alpha)
        # for i in range(len(d)):
        #     totalList.append(d[i])
        return list(d.values())