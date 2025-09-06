"""
Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109



"""

class Solution:
     def Four_sum(self,arr:list[int],target:int)->list[int]:
         arr.sort()
         result=[]
         for i in range(len(arr)-3):
             if i>0 and arr[i]== arr[i-1]:
                 continue
             for j in range(i+1,len(arr)-2):
                 if j> i+1 and arr[j]== arr[j-1]:
                     continue

                 k = j+1
                 n= len(arr)-1

                 while k < n:
                     current_sum= arr[i]+arr[j]+arr[k]+arr[n]

                     if current_sum==target:
                         result.append([arr[i],arr[j],arr[k],arr[n]])

                         while k < n and  arr[k]==arr[k+1]:
                             k+=1
                         while k < n and arr[n]==arr[n-1]:
                             n-=1
                         k+=1
                         n-=1
                     elif current_sum<target:
                          k+=1
                     else:
                         n-=1
         return result







def test_Four_sum():
    sol= Solution()
    assert sol.Four_sum([1,0,-1,0,-2,2],0)==[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    assert sol.Four_sum([1, 2, 3, 4, 5, 6],12)==[[1, 2, 3, 6],[1, 2, 4, 5]]
    assert sol.Four_sum([2, 2, 2, 2,2],8)==[[2,2,2,2]]
    assert sol.Four_sum([-2,-1,-1,1,1,2,2], -0) == [[-2,-1,1,2],[-1,-1,1,1]]





if __name__ == '__main__':
    test_Four_sum()