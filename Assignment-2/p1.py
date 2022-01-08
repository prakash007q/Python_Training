def lcp (arr):
    size = len(arr)
    if (size == 1):
      return arr[0]
    arr.sort()
    end  = min(len(arr[0]), len(arr[size -1]))
    i = 0
    if(i < end and arr[0][i] != arr[size -1][i]):
       return "There is no common prefix among the input strings"
    while (i < end and arr[0][i] == arr[size -1][i]):
       i = i+1
       prefix = arr[0][0:i]
       final_prefix_string = ""
       final_prefix_string += prefix
    return final_prefix_string
   
#Driver Code..
# input = ["flower","flow","flight"]
input = ["dog","racecar","car"]
# input = ["dog"]

#Function call..
print(lcp(input))