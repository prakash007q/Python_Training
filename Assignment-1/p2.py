
from itertools import combinations
def closeset_sum(arr,target):
   Combination_of_3pair = list(combinations(arr,3))
   for i in range(len(Combination_of_3pair)):
       result1 = (sum(Combination_of_3pair[i]))
       result2 = target - result1
       if result2 < target:
          print("The target value is",target,"and it's closest pairs are",Combination_of_3pair[i], "and result is",result1) 
      
#Driver Code...
arr = [-1,2,1,-4]
target = 1
#Function call...
closeset_sum(arr,target)


#from itertools import combinations
# def closeset_sum(arr,target):
#    Combination_of_3pair = list(combinations(arr,3))
#    for i in range(len(Combination_of_3pair)):
#        sum1 = [(sum(Combination_of_3pair[i]))]
#        difference = lambda sum1 : abs(target - sum1)
#        closest_values = min(sum1, key=difference)
#        print(closest_values,difference)
       
#       #  if target <= result2:
#       #     print("The sum that is closest to the target is ", result1,"and it's pairs are",Combination_of_3pair[i])
#       #  else:
#       #     print('0')
      
# #Driver Code...
# arr =[1,4,6,2]
# target = 5
# #Function call...
# closeset_sum(arr,target)



