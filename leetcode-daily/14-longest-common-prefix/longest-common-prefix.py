class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k=strs[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(k):
                k=k[:-1]
                if k=="":
                    return ""
        return k
            
        