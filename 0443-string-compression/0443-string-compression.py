class Solution:
    def compress(self, chars: List[str]) -> int:
        check = 0
        index = 0
        while check < len(chars):
            count = 0
            current = chars[check]
            while check < len(chars) and chars[check] == current:
                count += 1
                check += 1
            
            chars[index] = current
            
            if count > 1:
                for c in str(count):
                    index += 1
                    chars[index] = c
            
            index += 1
        
        return index
            