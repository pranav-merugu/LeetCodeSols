class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string not in result:
                result[sorted_string] = []

            result[sorted_string].append(string)
        
        return list(result.values())
                
    
          
            
        