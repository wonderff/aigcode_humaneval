def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # Initialize the number of collisions to 0
    collisions = 0

    # Create a list of cars moving left to right
    left_cars = [i for i in range(n)]

    # Create a list of cars moving right to left
    right_cars = [i for i in range(n)]

    # Iterate through the cars moving left to right
    for i in range(n):
        # Iterate through the cars moving right to left
        for j in range(n):
            # If the cars collide, increment the number of collisions
            if left_cars[i] == right_cars[j]:
                collisions += 1

    # Return the number of collisions
    return collisions