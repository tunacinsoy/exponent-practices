"""

Description:
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-28

Version:
    1.0.0

Algorithm Implementation:

  # CASE 1
  arr1 = [1,2,3,0,0,0]
  arr2 = [2,4,6]
  m = 3
  n = 3
  arr1 = [1,2,2,3,4,6]
                                                                         M
       L     M          L   M            L M            L M              L
  [1,2,3,0,0,0] -> [1,2,3,0,0,6] -> [1,2,3,0,4,6] -> [1,2,3,3,4,6] -> [1,2,2,3,4,6]

R
  [2,4,6]

  # CASE 2

L      M
  [6,7,8,6,7,8,9]
       R
  [1,2,3]


Complexities:
  Time: O(m + n), because destination pointer starts from (m+n-1), and goes back until it fully finishes nums1 array
  Space: O(1), we do modification in place, we do not use any other space
"""

from typing import List


class Solution:
    def merge_sorted_array(
        self, nums1: List[int], nums2: List[int], m: int, n: int
    ) -> None:
        nums1_pointer = m - 1
        dest_pointer = m + n - 1
        nums2_pointer = n - 1

        while nums2_pointer >= 0 and nums1_pointer >= 0:
            if nums2[nums2_pointer] >= nums1[nums1_pointer]:
                nums1[dest_pointer] = nums2[nums2_pointer]
                nums2_pointer -= 1
            else:
                nums1[dest_pointer] = nums1[nums1_pointer]
                nums1_pointer -= 1

            dest_pointer -= 1

        while nums2_pointer >= 0:
            nums1[dest_pointer] = nums2[nums2_pointer]
            dest_pointer -= 1
            nums2_pointer -= 1


# Test cases
def test_merge_sorted_array():
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 4, 6]
    m = 3
    n = 3
    solution.merge_sorted_array(nums1, nums2, m, n)
    assert nums1 == [1, 2, 2, 3, 4, 6]

    nums1 = [0, 0, 0]
    nums2 = [2, 4, 6]
    m = 0
    n = 3
    solution.merge_sorted_array(nums1, nums2, m, n)
    assert nums1 == [2, 4, 6]

    nums1 = []
    nums2 = []
    m = 0
    n = 0
    solution.merge_sorted_array(nums1, nums2, m, n)
    assert nums1 == []

    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    m = 3
    n = 3
    solution.merge_sorted_array(nums1, nums2, m, n)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    nums1 = [1]
    nums2 = []
    m = 1
    n = 0
    solution.merge_sorted_array(nums1, nums2, m, n)
    assert nums1 == [1]

    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    solution.merge_sorted_array(nums1, nums2, m, n)
    assert nums1 == [1]

    print("All test cases passed!")


# Run the tests
test_merge_sorted_array()
