class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myDict = {}
        answer = []
        indexCount = 0
        
        for num in nums:
            if num in myDict:
                answer.append(myDict[num])
                answer.append(indexCount)
                return answer

            else:
                myDict[target-num] = indexCount





            indexCount +=1
            
        return answer


        