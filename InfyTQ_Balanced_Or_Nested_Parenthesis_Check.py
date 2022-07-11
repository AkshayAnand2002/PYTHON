#A non-empty string input_str containing only brackets (,),{,},[,] it returns 
#output_str based on the following-
#input_str is properly nested then return 0
#input_str not properly nested return position of element in input_str-n+1
#input-{{[]}}}  output-7
# Defining the string
string = "{[()]}[]"
# Storing opening braces in list lst1
lst1 =['{', '(', '[']
# Storing closing braces in list lst2
lst2 =['}', ')', ']']
# Creating an empty list lst
lst =[]
# Creating dictionary to map
# closing braces to opening ones
Dict ={ ')':'(', '}':'{', ']':'['}
a = b = c = 0
# If first position of string contain
# any closing braces return 1
if string[0] in lst2:
	print(1)
else:
	# If characters of string are opening
	# braces then append them in a list
	for i in range(0, len(string)):
		if string[i] in lst1:
			lst.append(string[i])
			k = i + 2
		else:
			# When size of list is 0 and new closing
			# braces is encountered then print its
			# index starting from 1		
			if len(lst)== 0 and (string[i] in lst2):
				print(i + 1)
				c = 1
				break
			else:
				# As we encounter closing braces we map
				# them with theircorresponding opening
				# braces using dictionary and check
				# if it is same as last opened braces
				#(last element in list) if yes then we
				# delete that element from list
				if Dict[string[i]]== lst[len(lst)-1]:
					lst.pop()
				else:
					# Otherwise we return the index
					# (starting from 1) at which
					# nesting is found wrong
					print(i + 1)
					a = 1
					break
	# At end if the list is empty it
	# means the string is perfectly nested			
	if len(lst)== 0 and c == 0:
		print(0)
		b = 1
	if a == 0 and b == 0 and c == 0:
		print(k)
