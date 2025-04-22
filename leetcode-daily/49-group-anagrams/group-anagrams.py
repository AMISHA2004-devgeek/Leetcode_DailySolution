from collections import Counter ,defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        k=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            k[key].append(s)
        return list(k.values())




        