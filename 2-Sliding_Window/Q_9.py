"""

Given an array where the element at the index i represents the price of a stock on day i,
find the maximum profit that you can gain by buying the stock once and then selling it.
Note: You can buy the stock on one specific day and sell it on a different day to make a profit.
If no profit can be achieved, we return zero.

 """

class Solution:
    def most_profitable(self,stock):
        pass



def test_most_profitable():
    sol=Solution()
    assert sol.most_profitable([7,1,5,3,6,4])==5

    assert sol.most_profitable([7,6,4,3,1])==0

if __name__ == '__main__':
    test_most_profitable()