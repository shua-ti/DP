#coding=utf-8
#!/usr/bin/env python
"股票买卖问题"
#动态规划的遍历避免平方级操作

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        preprofit = [0] * len(prices)
        postprofit = [0] * len(prices)
        curmin = prices[0]
        for i in range(1, len(prices)):   #求出第i天之前的最大获利 相对之前的价格，第i天是卖出 低买高卖
            curmin = min(curmin, prices[i])
            preprofit[i] = max(preprofit[i - 1], prices[i] - curmin)
        curmax = prices[-1]
        for j in range(len(prices) - 2, -1, -1): #求出第i天以后的最大获利，相对之后的价格，第i天是买入
            curmax = max(curmax, prices[j])
            postprofit[j] = max(postprofit[j + 1], curmax - prices[j])
        return max(preprofit[i] + postprofit[i] for i in range(len(prices)))


if __name__=="__main__":
    s=Solution()
    prices=[10,4,14,25,78,56,67,89,40]
    print s.maxProfit(prices)




