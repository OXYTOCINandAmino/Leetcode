class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        hash_sol = set()
        
        #avoid duplicate nums[i]
        i_set = set()
        for i in range(0,len(nums)):
            # skip when nums[i] == num[i-1]
            if(nums[i] in i_set):
                continue
            
            # convert to 2 sum    
            L = []
            S = set()
            tar = - nums[i]                       
            for j in range(i+1, len(nums)):
                if(nums[j] in i_set):
                    continue
                if(tar - nums[j] in S):
                    L = [nums[i]]+[nums[j]]+[tar - nums[j]]
                    L.sort()
                    T = tuple(L)
                    if(T not in hash_sol):
                        hash_sol.add(T)
                        sol.append(L)
                S.add(nums[j])
            #mark num[i] as computed
            i_set.add(nums[i])
            
        return sol
                