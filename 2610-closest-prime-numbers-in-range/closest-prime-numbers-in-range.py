class Solution(object):
    def closestPrimes(self, left, right):
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p <= right:
            if is_prime[p]:
                for i in range(p * p, right + 1, p):
                    is_prime[i] = False
            p += 1

        prev = -1
        best = [-1, -1]
        min_gap = float('inf')

        for n in range(left, right + 1):
            if is_prime[n]:
                if prev != -1 and n - prev < min_gap:
                    min_gap = n - prev
                    best = [prev, n]

                prev = n

        return best
        