import math

def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    # Initialize the number of times the buckets need to be lowered to 0
    times = 0
    # Iterate through each row of the grid
    for row in grid:
        # Initialize the number of water units in the current row to 0
        water_units = 0
        # Iterate through each column of the current row
        for col in row:
            # If the current cell contains water, add the capacity of the bucket to the number of water units
            if col == 1:
                water_units += capacity
        # If the number of water units in the current row is greater than the capacity of the bucket,
        # calculate the number of times the bucket needs to be lowered and add it to the total number of times
        if water_units > capacity:
            times += math.ceil(water_units / capacity)
    # Return the total number of times the buckets need to be lowered
    return times