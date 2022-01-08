def longestPalindrome(s):
   if(len(s) <= 0):
      return "Given string is Empty!."
   else:
      dp = [[False for i in range(len(s))] for i in range(len(s))] #form square matrix 
      for i in range(len(s)):
         dp[i][i] = True               # set all diagonals as 1 ie., True
      start = 0
      max_length = 1
      for l in range(2,len(s)+1):  #Length = 5 # looping through (2,5+1 = 6) ie (2,3,4,5)
         for i in range(len(s)-l+1): # looping through (5-2,+1) ie,..(4) ie,,(0,1,2,3\\)
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
      return s[start:start+max_length]

#Function call.
print(longestPalindrome("babad"))
#Time Complexity O(n^2)