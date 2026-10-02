class Solution(object):
    def maxPoints(self, points):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if len(points) <= 2:
            return len(points)

        ans = 0

        for i in range(len(points)):
            slopes = {}

            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = gcd(dx, dy)

                dx //= g
                dy //= g

                slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

                ans = max(ans, slopes[slope] + 1)

        return ans