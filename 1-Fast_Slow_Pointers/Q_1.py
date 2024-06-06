"""Write an algorithm to determine if a number n
 is a happy number.
We use the following process to check if a given number is a happy number:
Starting with the given number n, replace the number with the sum of the squares of its digits.
Repeat the process until:
The number equals 1, which will depict that the given number n is a happy number.
The number enters a cycle, which will depict that the given number is not a happy number.
Return TRUE if
n
 is a happy number, and FALSE if not.

eg n = 23 is a happy number because: 2^2 + 3^2 = 13, 1^2 + 3^2 = 10, 1^2 + 0^2 = 1

 """

"""GPT SOLUTION EXPLANATION
Imagine you have a toy car that goes around a track. This track has two cars: one car moves slowly and the other one moves very fast. The slow car goes one step at a time, while the fast car goes two steps at a time.

Now, think about the number 𝑛
n as our starting point on this track. Here’s how the cars move:

Slow car: This car takes the number, breaks it into its digits, squares each digit, and then adds those squares together. For example, if the car starts at 23, it will do:

2^2 + 3^2 = 4 + 9 = 13
Fast car: This car does the same thing, but it does it twice before checking back with the slow car. So, if it starts at 23, it will do:

First step: 2^2 + 3^2 = 4 + 9 = 13
Second step: 1^2 + 3^2 = 1 + 9 = 10
Now, both cars keep moving around the track:

The slow car does one step at a time.
The fast car does two steps at a time."""

class Solution:
    def is_happy(self, n:int) -> bool:
        slow = n
        fast = n
        while True:
            slow = sum([int(i) ** 2 for i in str(slow)])
            fast = sum([int(i) ** 2 for i in str(sum([int(i) ** 2 for i in str(fast)]))])
            fast = sum([int(i) ** 2 for i in str(sum([int(i) ** 2 for i in str(fast)]))])
            if slow == fast:
                break
        return slow == 1






def test_is_happy():
    sol = Solution()
    assert sol.is_happy(23) == True
    assert sol.is_happy(12) == False
    assert sol.is_happy(19) == True
    assert sol.is_happy(2147483646) == False

if __name__ == '__main__':
    test_is_happy()
