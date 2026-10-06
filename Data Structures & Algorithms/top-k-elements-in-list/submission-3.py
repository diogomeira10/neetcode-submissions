class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        counts = {}
        freqs = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items():
            freqs[count].append(num)
            
        output = []
        
        for i in range(len(freqs) - 1, 0, -1):
            for j in freqs[i]:
                output.append(j)
                if len(output) == k:
                    return output
                
                

        
    
