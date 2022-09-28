
# Python3 program to find the most
# frequent element in an array.
def mostFrequent(arr, n):
  maxcount = 0;
  element_having_max_freq = 0;
  for i in range(0, n):
    count = 0
    for j in range(0, n):
      if(arr[i] == arr[j]):
        count += 1
    if(count > maxcount):
      maxcount = count
      element_having_max_freq = arr[i]
   
  return element_having_max_freq;
 
# Driver Code
arr = [40,50,30,40,50,30,30]
n = len(arr)
print(mostFrequent(arr, n))
#OUTPUT->30
