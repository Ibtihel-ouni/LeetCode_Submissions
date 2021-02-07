class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            
        l = [amount+1] * (amount+1)  # we can choose any other number to initialize the array
        l[0] = 0
        
        for coin in coins:
            for a in range(1, len(l)):
                if coin <= a:
                    l[a] = min (l[a] , l[a-coin] + 1)
                    
        return l[amount] if l[amount] != (amount+1) else -1 
