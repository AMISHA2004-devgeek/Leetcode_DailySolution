class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        c=0
        for num in arr:
            if num==0:
                c+=1
        i=len(arr)-1
        j=len(arr)-1+c
        while i!=j:
            if j<len(arr):
                arr[j]=arr[i]
            if arr[i]==0:
                j-=1
                if j<len(arr):
                    arr[j]=arr[i]
            j-=1
            i-=1






        
        