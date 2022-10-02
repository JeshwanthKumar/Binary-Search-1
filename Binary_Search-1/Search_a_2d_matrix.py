#Time Complexity: O(log mn) - Performing Binary search on row(m) and column(n)
#Space Complexity: O(1) - Searching in place

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)     #Initializing the no:of rows by finding the length of the matrix
        n = len(matrix[0])  #Initializing the no:of columns by finding the length of no:of rows
        
        low = 0     #Initialize low to 0
        high = (m*n)-1  #Initialize high to (no:rows*no:of columns) - 1
        
        while low<= high:       #Continue the loop until low is less than or equal to high 
            mid = low + (high - low)//2     #Finding the mid by dividing low+high//2 **low+(high-low)//2 is to prevent integer overflow
            num = matrix[mid//n][mid%n] #num is going to be the index of an element to be accessed in the matrix. We can the indices of the matrix by dividing mid by n to find the row and modulo mid by n to find the column. 
            
            if target == num:
                return True     #If target is the num then return True
            elif target < num:  #If the target is less than num point the high to mid -1 and ignore the right half
                high = mid -1   
            else:   #If the target is greater than num then point the low to mid + 1 and ignore the left part
                low = mid +1
            
        return False    #If the target is not found the matrix then return False