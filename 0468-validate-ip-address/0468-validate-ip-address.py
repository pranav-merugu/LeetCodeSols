class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        validHex = {"a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"}
        ip4 = queryIP.split('.')
        ip6 = queryIP.split(':')
        if len(ip4) == 4:
            for i in ip4:
                if not i.isdigit():
                    return "Neither"
                if len(i) > 3 or (i != '0' and i[0] == '0'):
                    return "Neither"
                if not (0 <= int(i) <= 255):
                    return "Neither"
            return "IPv4"

        if len(ip6) == 8:
            for i in ip6:
                if not (1 <= len(i) <= 4):
                    return "Neither"
                for c in i:
                    if not c.isdigit() and c not in validHex:
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"