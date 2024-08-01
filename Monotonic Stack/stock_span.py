# Solved on 01/08/2024
# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        # Monotonically increasing stack of price and span pairs.
        # -infinity is at the end of the stack to make comparisons more readable
        # than they'd be with checking if the stack is empty a bunch of times.
        self.stack = [(float('inf'), 0)]

    def next(self, price: int) -> int:
        # Price spans over all days of each (p, span) in the stack where p < price
        span = 1
        prev_price = self.stack[-1][0]
        while price >= prev_price:
            # Add prev_price's span to span and pop it
            span += self.stack.pop()[1]
            prev_price = self.stack[-1][0]
        self.stack.append((price,span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
