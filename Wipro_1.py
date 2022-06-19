//Wipro_1.c in python
n = int(input())
m1 = int(input())
p1 = int(input())
m2 = int(input())
p2 = int(input())
min_cost = -1
i = 0
while m1 * i <= n:
    count2 = n - i*m1
    if count2%m2 == 0:
            cost = int(p1 * i + p2 * (count2/m2))
            if cost < min_cost or min_cost == -1:
                min_cost = cost
    i += 1

if min_cost != -1:
        print(min_cost);
else:
        print("Invalid inputs");
