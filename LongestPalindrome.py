#T(N)=O(N)
#S(N)=O(N)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        midflag=False
        count=0
        di={}
        for i in s:
            if di.get(i,-1)==-1:
                di[i]=1
            else:
                di[i]+=1
        for val in di.values():
            if val%2==0:
                count+=val
            else:
                temp=(val//2)*2
                count+=temp
                if not midflag:
                    midflag=True
                    count+=1
        
        return count