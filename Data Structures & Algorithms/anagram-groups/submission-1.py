class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        final = []
        for word in strs: # convert list of words to dict of words to freq list
            alpha = [0] * 26
            for i in word:
                letterNum = ord(i) - 97 
                alpha[letterNum] += 1
                counter[word] = alpha
        counterList = []
        wordDict = {}
        for word, freq in counter.items(): # dict of words : freq to list of 
            if freq not in counterList:
                counterList.append(freq)
                # print(counterList)
            wordDict[word] = counterList.index(freq)
        d = defaultdict(list)
        for word, freqKey in wordDict.items():
            d[freqKey].append(word)
        totalList = list()
        for i in range(len(d)):
            totalList.append(d[i])
        print(totalList)
        # for word in strs:
        #     currList = list()
        #     if word in wordDict and 
        # print(counterList)
        # print(wordDict)
        # print(freqIdxSet)
        if len(totalList) == 0:
            return [[""]]
        return totalList