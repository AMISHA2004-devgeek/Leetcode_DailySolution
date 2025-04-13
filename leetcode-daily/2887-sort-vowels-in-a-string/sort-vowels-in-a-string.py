class Solution:
    def sortVowels(self, s: str) -> str:
        sortedlist= sorted((c for c in s if c.lower() in "aeiou"), reverse=True)
        res=[]
        for char in s:
            if char.lower() in "aeiou":
                res.append(sortedlist.pop())
            else:
                res.append(char)
        return "".join(res)

        