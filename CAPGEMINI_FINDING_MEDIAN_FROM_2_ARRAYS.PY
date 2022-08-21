'''
GIVEN DATA OF 2 ARRAYS WHICH CONTAIN DUPLICATED NOS. YOU NEED TO REMOVE DUPLICATED 
NOS AND FIND THE MEDIAN OF THE SORTED ARRAY.
INPUT-
ARRSY 1 WITH SPACES
ARRAY 2 WITH SPACES
OUTPUT-
FLOAT OR INT VALUE
SAMPLE INPUT--->
3 1 1 2 ->3 1 2  (REMOVED DUPLICATES)
4 3 3 2 1 -> 4 3 2 1
NOW COMBINING ELEMENTS FROM THE 2 ARRAYS ABOVE IN SORTED
MANNER AND FINDING MEDIAN.
1 1 2 2 3 3 4
OUTPUT->
2
'''
def median(arr1,arr2):
    arr=[]
    arr1=set(map(int,arr1))#set to avoid repetition of elements.
    arr2=set(map(int,arr2))
    for i in arr1:
        arr.append(i)
    for j in arr2:
        arr.append(j)
    arr.sort()
    median=len(arr)/2
    return arr[int(median)]
x=list(map(int,input().split(' ')))
y=list(map(int,input().split(' ')))
print(median(x,y))
