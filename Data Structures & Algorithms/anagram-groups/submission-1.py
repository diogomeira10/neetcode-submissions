class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = dict()
        
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]
        list = [value for value in anagrams.values()]
        
        return list