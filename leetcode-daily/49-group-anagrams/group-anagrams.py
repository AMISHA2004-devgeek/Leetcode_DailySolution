from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k = defaultdict(list)
        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            k[key].append(word)
        return(list(k.values()))



        