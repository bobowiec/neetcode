class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start_index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                start_index = index               
            stack.append((start_index, h))
        
        n = len(heights)
        for i, h in stack:
            area = h * (n - i)
            max_area = max(max_area, area)
        
        return max_area

    def largestRectangleAreaTwoPasses(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        left_most = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_most[i] = stack[-1]
            stack.append(i)
        
        stack = []
        right_most = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_most[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            left_most[i] += 1
            right_most[i] -= 1
            max_area = max(max_area, heights[i] * (right_most[i] - left_most[i] + 1))
        return max_area

    def largestRectangleAreaBF(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            height = heights[i]

            right_most = i + 1
            while right_most < n and heights[right_most] >= height:
                right_most += 1        

            left_most = i
            while left_most >= 0 and heights[left_most] >= height:
                left_most -= 1
            
            right_most -= 1
            left_most += 1
            max_area = max(max_area, height * (right_most - left_most + 1))
        return max_area

    def largestRectangleAreaBruteForce(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            min_height = heights[i]
            curr_max_area = min_height
            for j in range(i+1, n):
                min_height = min(min_height, heights[j])
                curr_max_area = max(curr_max_area, (j - i + 1) * min_height)
            max_area = max(max_area, curr_max_area)
        return max_area
        
