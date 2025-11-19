class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        # Prepare for multi-sources BFS starting with all nodes with indegree = 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        numVisited = 0

        while queue:
            node = queue.popleft()
            numVisited += 1

            # Decrement indegree by 1 for each neighbor
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                # Add neighbor to queue if its indegree becomes 0
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # numVisited == numCourses means we're able to visit all nodes
        # i.e. there's no cycle in the directed graph
        return numVisited == numCourses

# Time complexity: O(m + n) where n is the number of courses and m is the size of prerequisites
# Space complexity: O(m + n)