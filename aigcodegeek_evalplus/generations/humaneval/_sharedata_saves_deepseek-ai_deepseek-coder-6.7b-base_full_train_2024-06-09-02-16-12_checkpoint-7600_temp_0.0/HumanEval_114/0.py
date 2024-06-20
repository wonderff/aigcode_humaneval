def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum sum to be the maximum possible integer
    min_sum = float('inf')
    # Iterate through all possible sub-arrays
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # Calculate the sum of the current sub-array
            curr_sum = sum(nums[i:j+1])
            # Update the minimum sum if the current sum is smaller
            min_sum = min(min_sum, curr_sum)
    return min_sum