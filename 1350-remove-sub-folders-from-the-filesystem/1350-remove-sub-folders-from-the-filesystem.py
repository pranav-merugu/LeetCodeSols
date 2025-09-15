class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        result = [folder[0]]

        for i in range(1, len(folder)):
            check = result[-1] + "/"

            if not folder[i].startswith(check):
                result.append(folder[i])
        
        return result