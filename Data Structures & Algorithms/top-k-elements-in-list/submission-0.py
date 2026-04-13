class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = {}

        for num in nums:
            if num in storage:
                storage[num] = storage[num] + 1

            else:
                storage[num] = 1

        sorted_items = sorted(storage.items(), key=lambda x: x[1], reverse=True)

        return [num for num, freq in sorted_items[:k]]

            
        