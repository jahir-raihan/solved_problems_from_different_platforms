class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0

        current_window = set()

        for r in range(len(nums)):
            if r - l > k:
                current_window.remove(nums[l])
                l += 1

            if nums[r] in current_window:
                return True

            current_window.add(nums[r])
        return False