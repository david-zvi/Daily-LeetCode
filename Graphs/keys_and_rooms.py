# Solved on 30/06/2024
# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        self.visited = [False for _ in range(n)]
        def visit_room(num): # DFS
            if self.visited[num]: return
            self.visited[num] = True
            for room in rooms[num]: visit_room(room)
        visit_room(0)
        for visit in self.visited:
            if not visit: return False
        return True

