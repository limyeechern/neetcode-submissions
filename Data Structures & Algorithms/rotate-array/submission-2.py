class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end, arr):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        k %= len(nums)
        
        reverse(0, len(nums)-1, nums)
        reverse(0, k-1, nums)
        reverse(k, len(nums)-1, nums)
                
        
        