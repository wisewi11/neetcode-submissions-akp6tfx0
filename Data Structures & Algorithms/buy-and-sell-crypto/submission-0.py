class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        small = prices[0]
        

        answer = 0

        for num in prices:
            if num < small:
                small = num
            elif num > small:
                if ((num - small) > answer):
                    answer = num - small

        
        return answer


        