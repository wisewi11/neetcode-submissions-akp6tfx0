class Solution:
    def isValid(self, s: str) -> bool:
        joe = {     ")":"("       ,        "}":"{"       ,   "]":"["      }

        stack = []
        indexCount = 0

        while(indexCount <= (len(s)-1)):

            while ( indexCount <=(len(s)-1) and ((s[indexCount] =="(") or (s[indexCount] =="{") or (s[indexCount] =="[") )  ):
                stack.append(s[indexCount])

                indexCount +=1

            while (indexCount <=(len(s)-1) and ((s[indexCount] == ")") or (s[indexCount] =="}") or (s[indexCount] =="]"))   ):
                if (not stack):
                    return False
                if (stack[-1] == joe[s[indexCount]]):
                    
                    stack.pop()
                else:
                    return False


                indexCount +=1

        if (not stack):
            return True
        else:
            return False

        
        




        

        