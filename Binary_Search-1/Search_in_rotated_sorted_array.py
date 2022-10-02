#Time_Complexity: O(log n)
#Space_Complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 #Initialize low to 0
        high = len(nums)-1  #Initialize high to length of nums -1
        
        while low <= high:
            mid = low + (high-low) //2 #Integer overflow
            
            if nums[mid] == target: #If the target is equal to the mid element then return mid
                return mid
            
            if (nums[low] <= nums[mid]):  #If nums[low] is less than nums[mid] then left side of the array is sorted
                if (nums[low] <= target and target <= nums[mid]):   #If target is greater than nums[low] and less than nums[mid] then target is in the range, move the high pointer to mid -1
                    high = mid -1
                else:
                    low = mid +1    #Else the target is not in the range, so move the low pointer to mid +1 
            else:
                if (nums[mid] <= target and target <= nums[high]):  #Else the right side of the array is sorted
                    low = mid +1    #Move the low pointer to mid +1 
                else:
                    high =mid -1 #Else move the high pointer to mid -1
                    
        return -1   #If the target is not found then return -1
                