def two_sum (arr,target):
       hashtable = {}
       for i in range(len(arr)):
          result = target - arr[i]
          if result in hashtable:
               print('The two indexes are',[arr.index(result),i], "and it's values are",[result,arr[i]],"and their target =",target)
          else:
              hashtable[arr[i]] = arr[i]

#Driver Code...
arr = [2,7,11,15] 
target = 9
#function call...
two_sum (arr,target)
