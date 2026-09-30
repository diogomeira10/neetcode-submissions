class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_app = {}
        t_app = {}
        
        for char in s:
            if char not in s_app:
                s_app[char] = 1
            else:
                s_app[char] += 1
            
        for char in t:
            if char not in t_app:
                t_app[char] = 1
            else:
                t_app[char] += 1
                
        print(s_app)
        print(t_app)
        
        
        
        return s_app == t_app