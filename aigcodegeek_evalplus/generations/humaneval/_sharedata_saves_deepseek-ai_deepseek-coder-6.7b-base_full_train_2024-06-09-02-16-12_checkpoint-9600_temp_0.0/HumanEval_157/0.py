def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # The sides of the triangle
    sides = [a, b, c]
    # The maximum side
    max_side = max(sides)
    # The sum of squares of the other two sides
    sum_of_squares = sum([side**2 for side in sides if side != max_side])
    # The square of the maximum side
    square_of_max_side = max_side**2
    # Check if the triangle is right-angled
    return sum_of_squares == square_of_max_side