class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPoint = 0
        rightPoint = len(s) - 1
        
        while (rightPoint > leftPoint):
            while rightPoint >= 0 and  not(s[rightPoint].isalnum()):
                rightPoint -=1
            
            while leftPoint <= len(s) -1 and not(s[leftPoint].isalnum()):
                leftPoint +=1

            if (rightPoint > leftPoint):
                if (s[leftPoint].lower() != s[rightPoint].lower()):
                    return False

                rightPoint -=1
                leftPoint +=1



            



        
        return True




        