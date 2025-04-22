class Solution(object):
    def isValid(self, s):
        st=[]
        mapp={')':'(','}':'{',']':'['}
        for c in s:
            if c in mapp.values():
                st.append(c)
            elif c in mapp:
                if not st or st.pop()!=mapp[c]:
                    return False
        return not st
        