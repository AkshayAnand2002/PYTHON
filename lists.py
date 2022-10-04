#We can add, remove, count, sort, search, and do quite a few other things
#to python lists.


print('first we need an example list:')

x = [1,6,3,2,6,1,2,6,7]

print( '''lets add something. For that use .append,
which will add something to the end of the list''')

x.append(55)

print(x)


print("what if you have an exact place that you'd like to put something in a list?")

x.insert(2,33)

print(x)

# so the reason that went in the 3rd place, again, is because we start
# at the zero element, then go 1, 2.. .and so on.

# now we can remove things... .remove will remove the first instance
# of the value in the list. If it doesn't exist, there will be an error:
print('Lets remove the number 6 from the list')
x.remove(6)

print(x)

#next, remember how we can reference an item by index in a list? like:
print('Lets reference an item at index five, position six')
print(x[5])

print('We can also print the index of an element say for number 1')

print(x.index(1))

# now here, we can see that it actually returned a 0, meaning the
# first element was a 1... when we knew there was another with an index of 5.
# so instead we might want to know before-hand how many examples there are.
print("Lets print how many 1's are present in the list")
print(x.count(1))

# so we see there are actually 2 of them

print("we can also sort the list as well")
x.sort()

print(x)


print("what if these were strings? like: the list below")

y = ['Jan','Dan','Bob','Alice','Jon','Jack']
print(y)

y.sort()
print("That's how the sorted list of strings be printed ", y)

# noooo problemo!


# You can also just reverse a list, but, before we go there, we should note that
# all of these manipulations are mutating the list. keep in mind that any
# changes you make will modify the existing variable.




