class Solution(object):
    def romanToInt(self, s):
        roman_values = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}   
        t=0
        p=0
        for ch in reversed(s):
            curr=roman_values[ch]
            if curr <p:
                t-=curr
            else:
                t+=curr
            p=curr
        return t