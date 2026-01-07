class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_product = 0

    
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)


        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subtree_sum = left + right + node.val

           
            product = subtree_sum * (total - subtree_sum)
            self.max_product = max(self.max_product, product)

            return subtree_sum

        dfs(root)

        return self.max_product % MOD
