# def two_sum(arr, target):
#     pairs = [(a, b) for idx, a in enumerate(arr) for b in arr[idx + 1:]]
    
#     sum = []
#     for a, b in pairs:
#         sum.append(a+b)
    
#     difference = lambda sum : abs(target - sum)
#     closest_values = min(sum, key=difference)
#     print(pairs[sum.index(closest_values)])

# two_sum(arr=[1,6,-3,4,7,8,3], target=2)

a = ["",'']
# a = ""
print(len(a))