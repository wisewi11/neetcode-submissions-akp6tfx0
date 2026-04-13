class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer, rightPointer = 0, len(numbers) -1

        while leftPointer < rightPointer:
            curSum = numbers[leftPointer] + numbers[rightPointer]

            if curSum > target:
                rightPointer -=1
            elif curSum < target:
                leftPointer +=1
            else:
                return [leftPointer + 1, rightPointer + 1]


        return []


        