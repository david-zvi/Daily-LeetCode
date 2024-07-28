# Solved on 28/07/2024
# https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        results = []
        products.sort()
        n = len(searchWord)
        for i in range(n):
            # Uses binary search to find smallest index in products where
            # each product is <= than prefix lexicographically
            j = bisect_left(products, searchWord[:i+1])
            results.append([product for product in products[j:j+3] if product.startswith(searchWord[:i+1])])
        return results
