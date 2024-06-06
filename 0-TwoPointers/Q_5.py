"""Given an array, colors, which contains a combination of the following three elements:

0(representing red)
1(representing white)
2(representing blue)

Sort the array in place so that the elements of the same color are adjacent,
with the colors in the order of red, white, and blue.
 To improve your problem-solving skills, do not utilize the built-in sort function.

 eg colors = [1,0,2,1,2,2] output = [0,1,1,2,2,2]

 colors= [0,1,1,2,0,2,0,2,1,2] output = [0,0,0,1,1,1,2,2,2,2]

 """

class Solution:
    def sortColors(self, colors: list) -> list:
        start = 0
        end = len(colors) - 1
        current = 0
        while current <= end:
            if colors[current]== 0:
                colors[start],colors[current]= colors[current],colors[start]
                current+=1
                start+=1
            elif colors[current]==1:
                 current+=1

            elif colors[current]==2:
                 colors[current],colors[end]= colors[end],colors[current]
                 end-=1
        return colors

def test_sort_colors():
    sol=Solution()
    assert sol.sortColors([1,0,2,1,2,2]) == [0,1,1,2,2,2]
    assert sol.sortColors([0,1,1,2,0,2,0,2,1,2]) == [0,0,0,1,1,1,2,2,2,2]

if __name__ == '__main__':
    test_sort_colors()