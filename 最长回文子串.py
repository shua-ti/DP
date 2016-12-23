#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-23 16:15:41
# @Author  : wanpeng 
"最长回文子串"
def longestPalindrome(s):
	if len(s) < 2:
		return s
	def helper(s,i,j,maxlen,lo):
		while i>=0 and j<len(s) and s[i]==s[j]:
			i-=1
			j+=1
		if maxlen<j-i-1:
			maxlen=j-i-1
			lo=i+1
		return maxlen,lo
	maxlen=lo=0

	for k in range(len(s)-1):
		maxlen,lo=helper(s, k, k, maxlen, lo)
		maxlen,lo=helper(s, k, k+1, maxlen, lo)
	return s[lo:lo+maxlen]


if __name__=="__main__":
	print longestPalindrome('abbacab')

