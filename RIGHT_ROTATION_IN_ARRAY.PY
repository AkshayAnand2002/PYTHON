# Function to right-rotate a list by one position
def rightRotateByOne(A):
    last = A[-1]
    for i in reversed(range(len(A) - 1)):
        A[i + 1] = A[i]
    A[0] = last
# Function to right-rotate a list by `k` positions
def rightRotate(A, k):
    # base case: invalid input
    if k < 0 or k >= len(A):
        return
    for i in range(k):
        rightRotateByOne(A)
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rightRotate(A, k)
    print(A)
#OUTPUT-> [5, 6, 7, 1, 2, 3, 4]
