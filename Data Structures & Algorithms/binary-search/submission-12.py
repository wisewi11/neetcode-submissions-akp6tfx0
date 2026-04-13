class Solution:
    def search(self, nums: List[int], target: int) -> int:
        Findable = True
        left = 0
        right = len(nums) - 1
        
        while(Findable):
            mid = (right+left)//2
            
            if (right == left):
                Findable = False
            if (target == nums[mid]):
                return mid

            if (target > nums[mid]):
                left = mid +1 

            elif (target < nums[mid]):
                right = mid 

  
        return -1


        

