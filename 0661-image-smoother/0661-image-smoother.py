class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        newImg = [[0] * len(img[0]) for _ in range(len(img))]
        translations = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for row in range(len(img)):
            for col in range(len(img[0])):
                average = img[row][col]
                validCount = 1
                for t in translations:
                    tRow = row + t[0]
                    tCol = col + t[1]
                    if (tRow >= 0 and tRow < len(img)) and (tCol >= 0 and tCol < len(img[0])):
                        average += img[tRow][tCol]
                        validCount += 1
                average = average // validCount
                newImg[row][col] = average
        return newImg
