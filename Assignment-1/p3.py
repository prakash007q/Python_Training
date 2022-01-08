def median(arr1,arr2):
    merged_arr = arr1+arr2
    merged_arr.sort()
    length = len(merged_arr)
    index = length // 2
    if length % 2 == 1:
        print("Merged array = ",sorted(arr1 + arr2),"and median is",(merged_arr)[index])
    else:
        print("Merged array = ",sorted(arr1 + arr2),"and median is",(merged_arr[index] + merged_arr[index -1])/ 2)
    
  

#Driver code..
arr1=[1,2]
arr2=[3,4]
#Function Call..
median(arr1,arr2)

