class Solution:
    def secondHighest(self, s: str) -> int:
        k=set()
        for ch in s:
            if ch.isdigit():
             k.add(int(ch))
        k=sorted(k,reverse=True)
        return k[1] if len(k)>1 else -1
        