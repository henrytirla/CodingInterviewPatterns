"""

Given an array where the element at the index i represents the price of a stock on day i,
find the maximum profit that you can gain by buying the stock once and then selling it.
Note: You can buy the stock on one specific day and sell it on a different day to make a profit.
If no profit can be achieved, we return zero.

 """

class Solution:
    def most_profitable(self,stock):
        max_profit=0
        min_price=float("inf")


        for price in stock:
            min_price=min(min_price,price)
            profit=price-min_price
            max_profit=max(max_profit,profit)
        return max_profit



def test_most_profitable():
    sol=Solution()
    assert sol.most_profitable([7,1,5,3,6,4])==5

    assert sol.most_profitable([7,6,4,3,1])==0
    assert sol.most_profitable([1,2,4,2,5,7,2,4,9,0,9])==9

if __name__ == '__main__':
    test_most_profitable()