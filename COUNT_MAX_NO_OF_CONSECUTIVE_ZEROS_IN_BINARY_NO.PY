#COUNT_MAX_NO_OF_CONSECUTIVE_ZEROS_IN_BINARY_NO.
s = "100001000000"
zeros = 0
max_zeros = 0
for i in range(len(s)):
    if s[i] == "0":
        zeros += 1
        max_zeros = max(max_zeros, zeros)
    else:
        zeros = 0 #zeros counter is set to 0 as not consecutive.
print(max_zeros)
#Output = 3
