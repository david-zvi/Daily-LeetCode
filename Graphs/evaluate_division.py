# Solved on 03/07/2024
# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.adjecency_dict = dict()
        self.visited = None
        self.query = None
        self.cur_quotient = 1
        self.found_path = False
        self.answers = []
        self.index_map = {tuple(equation) : index for index, equation in enumerate(equations)}

        # Create adjecency lists
        for equation in equations:
            for i in range(2):
                if equation[i] not in self.adjecency_dict:
                    self.adjecency_dict[equation[i]] = []
                self.adjecency_dict[equation[i]].append(equation)

        def dfs(val):
            if self.found_path or self.visited[val]: return
            self.visited[val] = True
            for neighbor in self.adjecency_dict[val]:
                n = tuple(neighbor)
                if self.found_path: break
                reverse = True if n[1] == val else False
                if reverse: 
                    self.cur_quotient /= values[self.index_map[n]]
                    q = n[0]
                else: 
                    self.cur_quotient *= values[self.index_map[n]]
                    q = n[1]
                if q == self.query[1]: self.found_path = True
                dfs(q)
                if not self.found_path:
                    if reverse: self.cur_quotient *= values[self.index_map[n]]
                    else: self.cur_quotient /= values[self.index_map[n]]

        for query in queries:
            if not (query[0] in self.adjecency_dict and query[1] in self.adjecency_dict):
                self.answers.append(-1)
                continue
            self.query = query
            self.cur_quotient = 1
            self.found_path = False
            self.visited = {key: False for key in self.adjecency_dict}
            dfs(self.query[0])
            self.answers.append(self.cur_quotient if self.found_path else -1)
        return self.answers
