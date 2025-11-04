class Solution:
    def compress(self, chars: List[str]) -> int:
        check = 0
        while check < len(chars):
            length = check + 1
            count = 1
            while length < len(chars) and chars[length] == chars[check]:
                count += 1
                chars.pop(length)
            
            if 1 < count < 10:
                chars.insert(length, str(count))
                check = length + 1
            elif count >= 10:
                res = count
                check = length
                while res > 0:
                    chars.insert(length, str(res % 10))
                    res = res // 10
                    check += 1
            else:
                check = length
        
        return len(chars)
            