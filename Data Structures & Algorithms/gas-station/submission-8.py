class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        c_gas = 0
        c_max = 0
        c_idx = 0
        for i in range(len(gas)):
            c_gas += gas[i] - cost[i]
            c_max = max(0, c_max + (gas[i] - cost[i]))
            if c_max == 0:
                c_idx = (i+1) % len(gas)
        if c_gas >= 0:
            return c_idx
        return -1