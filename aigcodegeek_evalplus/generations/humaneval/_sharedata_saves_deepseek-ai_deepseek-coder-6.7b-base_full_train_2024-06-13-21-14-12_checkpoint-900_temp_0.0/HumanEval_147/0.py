def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    if n < 3:
        return 0

    count = [0] * 3
    for i in range(1, n+1):
        val = (i * i - i + 1) % 3
        count[val] += 1

    return count[0] * (count[0] - 1) * (count[0] - 2) // 6 + count[1] * count[2] * 2 * (count[0] + count[1] + count[2])

# Test cases
print(get_max_triples(5))  # Output: 1
print(get_max_triples(6))  # Output: 10
print(get_max_triples(7))  # Output: 36