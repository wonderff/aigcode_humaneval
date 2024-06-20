def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum sum to be the maximum possible integer value
    min_sum = float('inf')
    
    # Iterate through all possible sub-arrays
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # Calculate the sum of the current sub-array
            sub_array_sum = sum(nums[i:j+1])
            
            # Update the minimum sum if the current sub-array sum is smaller
            min_sum = min(min_sum, sub_array_sum)
    
    return min_sum