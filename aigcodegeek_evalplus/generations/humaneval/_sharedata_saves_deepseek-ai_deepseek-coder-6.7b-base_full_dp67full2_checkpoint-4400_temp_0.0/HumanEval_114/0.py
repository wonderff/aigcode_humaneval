def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum sum as the first element of the array
    min_sum = nums[0]

    # Initialize the current sum as the first element of the array
    current_sum = nums[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Update the current sum by adding the current element
        current_sum += nums[i]

        # If the current sum is smaller than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum

        # If the current sum is greater than 0, reset it to 0
        if current_sum > 0:
            current_sum = 0

    return min_sum