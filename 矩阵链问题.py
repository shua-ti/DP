#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-18 12:34:22
# @Author  : wanpeng
# @Version : 1.0
"矩阵链问题"

P=[30,35,15,5,10,20,25]
size=len(P)-1  #矩阵个数
dp=[[0 for i in range(size)] for j in range(size)]

def matrixchain(P):
	
	for gap in range(1,size):
		for i in range(size-gap):
			j=i+gap
			dp[i][j]=min([dp[i][k]+dp[k+1][j]+P[i]*P[k+1]*P[j+1] for k in range(i,j)])
	return dp[0][size-1]


if __name__=="__main__":
	print matrixchain(P)
