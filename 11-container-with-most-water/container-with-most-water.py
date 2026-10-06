class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        answer = 0

        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1

            if area > answer:
                answer = area

        return answer