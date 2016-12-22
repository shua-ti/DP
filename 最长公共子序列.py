#-*-coding=utf-8-*-
#/usr/bin/env python
"最长公共子序列"

from bisect import bisect

def lcs(a,b):
    m,n = len(a),len(b)
    res = [[-1 for i in range(n+1)] for j in range(m+1)]  #中间结果矩阵 [m+1][n+1]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                res[i][j]=0
            elif a[i-1]==b[j-1]:
                res[i][j]=1+res[i-1][j-1]
            else:
                res[i][j]=max(res[i-1][j],res[i][j-1])
    return res


def findseq(res,a):
    m,n=len(res),len(res[0])
    i,j = m-1,n-1
    seq =[0]* len(a)
    while i!=0 and j!=0:
        if res[i][j]==res[i-1][j]:
            i-=1
        elif res[i][j]==res[i][j-1]:
            j-=1
        else:
            seq[i-1]=1
            j-=1
            i-=1
    for i in range(len(a)):
        if seq[i]==1:
            print a[i],

if __name__=="__main__":
    a = 'ABCBDAB'
    b = 'BDCABA'
    findseq(lcs(a,b),a)
