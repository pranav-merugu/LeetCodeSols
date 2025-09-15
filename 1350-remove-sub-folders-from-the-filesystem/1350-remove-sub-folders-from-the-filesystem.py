class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        result = []

        for fol in folder:
            if len(result) == 0: #first one is automatically a parent folder
                result.append(fol)
            else:
                if len(fol) > len(result[-1]) and fol[0:len(result[-1])] == result[-1] and fol[len(result[-1])] == "/":
                    continue
                else:
                    result.append(fol)

        return result