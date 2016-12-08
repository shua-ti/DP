#coding=utf-8
#!/usr/bin/env python
"背包问题"

n = 5
c = 10    #背包承受最大重量
w = [2, 2, 6, 5, 4] #物品的重量
v = [6, 3, 5, 4, 6] #物品的价值

#刻画的问题是物品i是否放入包中
def bag(n, c, w, v):
    res = [[-1 for j in range(c + 1)] for i in range(n + 1)]#初始化矩阵res[n+1][c+1]
    for j in range(c + 1):
        res[0][j] = 0          #k=0 没有物品放入价值初始化为0
    for i in range(1, n + 1): #
        for j in range(1, c + 1):
            res[i][j] = res[i - 1][j]  #由优化函数递推式可得出
            if j >= w[i - 1] and res[i][j] < res[i - 1][j - w[i - 1]] + v[i - 1]:
                res[i][j] = res[i - 1][j - w[i - 1]] + v[i - 1]
    return res

#根据递推方程推算物品是否放入包中
def show(n, c, w, res):
    print'最大价值为:', res[n][c]
    x = [False for i in range(n)]
    j = c
    for i in range(n,0,-1):
        if res[i][j] > res[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('选择的物品为:')
    for i in range(n):
        if x[i]:
            print'第', i, '个'


if __name__ == '__main__':

            res = bag(n, c, w, v)
            show(n, c, w, res)
