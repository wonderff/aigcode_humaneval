def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Convert the integer N to binary
    binary_N = bin(N)[2:]
    
    # Initialize the sum of digits to 0
    sum_of_digits = 0
    
    # Iterate through each digit in the binary representation
    for digit in binary_N:
        # Convert the digit back to integer and add it to the sum
        sum_of_digits += int(digit)
    
    # Return the sum of digits as a binary string
    return binary_N