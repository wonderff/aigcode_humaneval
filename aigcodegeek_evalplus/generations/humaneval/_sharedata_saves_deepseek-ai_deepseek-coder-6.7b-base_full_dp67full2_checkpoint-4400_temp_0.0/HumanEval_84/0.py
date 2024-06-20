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
    binary = bin(N)
    
    # Remove the '0b' prefix from the binary representation
    binary = binary[2:]
    
    # Calculate the sum of the digits in binary
    digit_sum = sum(int(digit) for digit in binary)
    
    # Return the sum as a binary string
    return bin(digit_sum)[2:]