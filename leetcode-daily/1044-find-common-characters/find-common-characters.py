from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count=Counter(words[0])
        for w in range(1,len(words)):
            count&=Counter(words[w])
        res=[]
        for key,val in count.items():
            res.extend((key)*val)
        return res