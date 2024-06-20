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
    # Step 1:  Initialize a variable to keep track of the number of times the buckets need to be lowered
    times = 0
    
    # Step 2:  Iterate through each row of the grid
    for row in grid:
        # Step 3:  Initialize a variable to keep track of the number of times the bucket needs to be lowered for each row
        row_times = 0
        
        # Step 4:  Iterate through each element in the row
        for element in row:
            # Step 5:  If the element is 1, increment the number of times the bucket needs to be lowered
            if element == 1:
                row_times += 1
        
        # Step 6:  Add the number of times the bucket needs to be lowered for the current row to the total number of times
        times += row_times // capacity
    
    # Step 7:  Return the total number of times the buckets need to be lowered
    return times