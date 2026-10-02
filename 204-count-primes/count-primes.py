class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        is_prime = bytearray(b'\x01') * n
        is_prime[0] = is_prime[1] = 0

        p = 2

        while p * p < n:
            if is_prime[p]:
                is_prime[p * p:n:p] = b'\x00' * (((n - 1 - p * p) // p) + 1)
            p += 1

        return sum(is_prime)