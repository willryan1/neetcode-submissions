class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_sum = 0
        m_sum = float('-inf')
        for i in range(len(nums)):
            c_sum += nums[i]
            m_sum = max(m_sum, c_sum)
            
            if c_sum < 0:
                c_sum = 0
        return m_sum