class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        
        endTime = 0
        numClips = 0
        i = 0

        while endTime < time:
            farthestReach = endTime
            while i < len(clips) and clips[i][0] <= endTime:
                farthestReach = max(farthestReach, clips[i][1])
                i += 1
            
            if endTime == farthestReach:
                return -1

            endTime = farthestReach
            numClips += 1
        
        return numClips
            

        