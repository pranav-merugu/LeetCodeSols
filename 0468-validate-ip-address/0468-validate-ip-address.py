class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        validHex = {"a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"}
        if ":" in queryIP:
            sections = queryIP.split(":")
        else:
            sections = queryIP.split(".")
        if len(sections) == 4:
            for sec in sections:
                for char in sec:
                    if not char.isnumeric():
                        return "Neither"
                if len(sec) == 0 or (sec != '0' and sec[0] == '0') or int(sec) < 0 or int(sec) > 255:
                    return "Neither"
            return "IPv4"
        elif len(sections) == 8:
            for sec in sections:
                if len(sec) < 1 or len(sec) > 4:
                    return "Neither"
                for char in sec:
                    if not char.isnumeric() and char not in validHex:
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"