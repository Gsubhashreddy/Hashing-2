#T(n) = O(N)
#S(n) = O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cs=[]
        temp=0
        di={}
        di[0]=1
        count=0
        for i in nums:
            temp+=i
            if di.get(temp-k,None)!=None:
                count+=di[temp-k]
            if di.get(temp,None)!=None:
                di[temp]=di[temp]+1
            else:
                 di[temp]=1
                
        return count