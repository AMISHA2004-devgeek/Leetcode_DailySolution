class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        k=list(s)
        i=0
        j=len(s)-1
        while i <j:
            if k[j] in vowels:
                if k[i] in vowels:
                    k[j],k[i]=k[i],k[j]
                    i+=1
                    j-=1
                else:
                    i+=1
            else:
                j-=1
        return "".join(k)
            
        