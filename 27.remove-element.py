class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_index =0

        for i in range(len(nums)):
            if nums[i] !=val:
                nums[new_index] = nums[i]
                new_index+=1           
              
        return new_index

