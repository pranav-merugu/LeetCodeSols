class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        '''
        Solution 1: Greedy
        
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
        '''

        dp = [float('inf')] * 101 #some intervals can have a time that exceeds the given time, so to be safe have the DP be the max possible size
        dp[0] = 0

        for start, end in clips:
            for i in range(start, end + 1):
                dp[i] = min(dp[i], dp[start] + 1)
        
        if dp[time] == float('inf'):
            return -1
        else:
            return dp[time]


        