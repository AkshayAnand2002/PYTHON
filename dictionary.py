
# Dictionary of names and ages. 
exDict = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}

print(exDict)

# How old is Jack?

print(exDict['Jack'])


# We find a new person that we want to insert:

exDict['Tim'] = 14

print(exDict)

# Tim just had a birthday though so lets update his age!

exDict['Tim'] = 15

print('List with updated age of Tim'"\n",exDict)


# Then Tim died.
print('Tim is no more, so...')
del exDict['Tim']
print(exDict)

# next we want to track hair color

exDict = {'Jack':[15,'blonde'],'Bob':[22, 'brown'],'Alice':[12,'black'],'Kevin':[17,'red']}

print('\nJack has'+' '+exDict['Jack'][1]+ " "+'hair')

