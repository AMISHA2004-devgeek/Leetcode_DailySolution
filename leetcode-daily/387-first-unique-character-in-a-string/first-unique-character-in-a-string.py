class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt=Counter(s)
        visited=defaultdict(int)
        for i,ch in enumerate(s):
            if ch not in visited:
                visited[ch]=i
        for key,val in cnt.items():
            if val==1:
                return visited[key]
        return -1
            

        