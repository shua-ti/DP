public class Solution{
	public int lenofLIS(int[] nums){
		int[] dp =new int[nums.length];
		int len=0;
		for(int val : nums){
             int idx=Array.binsearch(dp,0,len,val);
             if (idx<0) idx=-(idx+1);
             dp[idx]=val;
             if(idx==len) len++;
		}
        return len;
	}
}
