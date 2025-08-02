#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #1.calculate len
        lens=len(s)
        lenp=len(p)
        ans=[]
        if lens<lenp:
            return []
        
        curwin=s[:lenp]
        curc=Counter(curwin)
        counterp=Counter(p)
        if curc==Counter(p):
            ans.append(0)
        
        #slide window
        for i in range(lenp,lens):
            leftchar=s[i-lenp]
            curc[leftchar]-=1
            if curc[leftchar]==0:
                del curc[leftchar]

            curc[s[i]]+=1
            if curc==counterp:
                ans.append(i-lenp+1)

        return ans



            

            

    


        
        
# @lc code=end

