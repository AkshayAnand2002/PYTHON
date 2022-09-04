def rearrange(arr):
    p = 0
    b = 0
    for i in range(len(arr)):
        if b == 1:
            b -= 1
        elif arr[i] < 0:
            arr[i], arr[p] = arr[p], arr[i]
            if p > i:
                b += 1
            p += 2
    return arr


array = [2, 3, -4, -1, 6, -9]
print("After Rearranging :", rearrange(array))
#OUTPUT- After Rearranging : [-4, 3, -1, 2, -9, 6]
