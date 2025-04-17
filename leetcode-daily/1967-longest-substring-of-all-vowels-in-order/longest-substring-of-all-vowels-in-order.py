
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        l=0
        vowel="aeiou"
        maxlen=0
        seen=set()

        for r in range(len(word)):
            if r>0 and word[r]<word[r - 1]:
                l=r
                seen.clear()

            seen.add(word[r])

            if set(vowel)==seen:
                maxlen=max(maxlen, r - l + 1)

        return maxlen

        