#-*-coding=utf-8-*-
#!/usr/bin/env python
"计数求和问题"


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {} #保留中间结果，快速查询
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)

    def helper(self, nums, desiredTotal):
        hash = str(nums)          #字符串是可哈希对象,便于快速查找
        if hash in self.memo:     #从保留的结果中直接是否有匹配的模式
            return self.memo[hash]

        #如果最大的数 >=desiredTotal
        if nums[-1] >=desiredTotal:
            return True

        for i in range(len(nums)):
            if  not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):#对方拿到的模式不能赢
                self.memo[hash] = True
                return True
        self.memo[hash] = False #自己选取任意数字后，对方都能赢，表明这局自己肯定输了
        return False

if __name__=="__main__":
    game = Solution()
    print game.canIWin(4,7)