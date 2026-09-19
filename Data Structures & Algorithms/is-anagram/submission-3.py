class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_list = list(s)
        t_list = list(t)
        
        # Sort both lists alphabetically
        s_list.sort()
        t_list.sort()
        
        # Directly compare the sorted lists
        return s_list == t_list
