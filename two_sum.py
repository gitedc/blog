import copy
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        for i in nums:
            list2 = copy.deepcopy(nums)
            list2.remove(i)
            for j in list2:
                if i + j == target:
                    a = nums.index(i)
                    b = nums.index(j)
                    ret.append(a)
                    ret.append(b)
                    print(ret)
                    return ret



if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([1, 2, 3, 4], 5)