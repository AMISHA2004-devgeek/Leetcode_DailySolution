class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        c=0
        currsum=0
        for r in range(len(arr)):
            currsum+=arr[r]
            while r-l+1 ==k:
                if currsum/k>=threshold:
                    c+=1
                currsum-=arr[l]
                l+=1
        return c

        