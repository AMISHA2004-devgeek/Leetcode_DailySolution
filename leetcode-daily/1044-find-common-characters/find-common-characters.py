class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        k=Counter(words[0])
        for i in range(1,len(words)):
            k&=Counter(words[i])
        res=[]
        for key,v in k.items():
            res.extend((key)*v)
        return res