class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if (target - num[i]) in map:
                return (map[target-num[i]]+1, i+1)
            else:
                map[num[i]] = i
        
        return None