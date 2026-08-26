class Solution(object):
    def singleNumber(self, nums):
        return int(''.join([str(i) if nums.count(i)==1 else '' for i in nums]))
