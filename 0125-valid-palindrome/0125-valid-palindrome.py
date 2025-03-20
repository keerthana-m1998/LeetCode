import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #convert to Lower case
        regex = "[^A-Za-z0-9]" #Remove alphanumeric CHARS
        s = re.sub(regex,"",s) #Using Import re, substitute regex
        s = s.replace(" ","")   # removing whitespace
        return s == s[::-1] #Palindrome check
        
    #     l,r=0,len(s)-1 # left and right pointer
    #     while (l<r): #Ignoring no alphanumeric values
    #         while l<r and not self.alphanumeric(s[l]):
    #             l+=1
    #         while r>l and not self.alphanumeric(s[r]):
    #             r-=1

            # palindrom check for lower cases
    #         if s[l].lower()!=s[r].lower():
    #             return False
    #         l+=1
    #         r-=1
    #     return True
    
        #Function to check for alphanumeric values
    # def alphanumeric(self,c):
    #     return (ord("A")<=ord(c)<=ord("Z") or 
    #             ord("z")<=ord(c)<=ord("z") or
    #             ord("0")<=ord(c)<=ord("9"))