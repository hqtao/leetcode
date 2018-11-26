# -*- coding: utf-8 -*-
#已通过

nums = [3,3,12,20,23,45,]
target = 68

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for k,v in enumerate(nums):
            dic[k] = v
        output = []
        U = set(dic.keys())
        for i in set(dic.keys()):
            U -= {i}
            for j in U:
                if dic[i] + dic[j] == target:
                    output.append(i)
                    output.append(j)
                    return sorted(set(output))

s = Solution().twoSum(nums,target)
print(s)







