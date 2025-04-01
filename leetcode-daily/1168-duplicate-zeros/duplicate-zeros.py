class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        count=0
        for num in arr:
            if num==0:
                count=count+1
        i=len(arr)-1
        j=len(arr)-1+count
        while i!=j:
            if j<len(arr):
                arr[j]=arr[i]
            if arr[i]==0:
                j=j-1
                if j<len(arr):
                    arr[j]=0
            i=i-1
            j=j-1





        
        