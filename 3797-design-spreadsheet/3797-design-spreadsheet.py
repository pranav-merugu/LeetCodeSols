class Spreadsheet:

    def __init__(self, rows: int):
        self.ss = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}
        for col in self.ss.keys():
            self.ss[col] = [0] * rows

    def setCell(self, cell: str, value: int) -> None:
        self.ss[cell[0]][int(cell[1:]) - 1] = value

    def resetCell(self, cell: str) -> None:
        self.ss[cell[0]][int(cell[1:]) - 1] = 0
        
    def getValue(self, formula: str) -> int:
        plusIndex = formula.index('+')
        val1 = 0

        if formula[1].isalpha():
            val1 = int(self.ss[formula[1]][int(formula[2:plusIndex]) - 1])
        else:
            val1 = int(formula[1:plusIndex])

        val2 = 0

        if formula[plusIndex + 1].isalpha():
            val2 = int(self.ss[formula[plusIndex+1]][int(formula[plusIndex+2:]) - 1])
        else:
            val2 = int(formula[plusIndex+1:])

        return val1 + val2




# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)