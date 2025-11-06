class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image

        R, C = len(image), len(image[0])
        stack = [(sr, sc)]
        color = image[sr][sc]

        while stack:
            r, c = stack.pop()
            if image[r][c] == color:
                image[r][c] = newColor
                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in neighbors:
                    if 0 <= nr < R and 0 <= nc < C:
                        stack.append((nr, nc))

        return image

# Time complexity: O(mn)
# Space complexity: O(mn)