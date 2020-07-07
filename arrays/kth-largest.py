class Solution:
    def partition(self, arr, l, r):
        x = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        arr[i], arr[r] = arr[r], arr[i]
        return i
    
    def kthSmallest(self, arr, l, r, k):
        if k > 0 and k <= r - l + 1:
            pos = self.partition(arr, l, r)
            
            if pos - l == k - 1:
                return arr[pos]
            if pos - l > k - 1:
                return self.kthSmallest(arr, l, pos - 1, k)
            return self.kthSmallest(arr, pos + 1, r, k - pos + l - 1)
        
        return float('inf')

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.kthSmallest(nums, 0, n - 1, n - k + 1)
