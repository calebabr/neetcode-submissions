class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre='1'
        after=''
        result=[]
        for i in range(1,len(nums)):
            after+=str(nums[i])+'*'
        result.append(eval(pre)*eval(after.rstrip('*')))
        for i in range(1,len(nums)):
            pre+='*'+str(nums[i-1])
            l=len(str(nums[i])+'*')
            after=after[l:]
            result.append(eval(pre)*eval(after.rstrip('*') or '1'))
        return result
        
