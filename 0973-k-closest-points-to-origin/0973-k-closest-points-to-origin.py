class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points
        heap = [(-self.squaredDistance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)

        for i in range(k, len(points)):
            dist = -self.squaredDistance(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))

        return [points[i] for (_, i) in heap]

    def squaredDistance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2

# Time complexity: O(n * log k)
# Space complexity: O(k)