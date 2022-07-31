#Algorithm-
#1) Reverse the given linked lists l1 and l2.
#2) Convert the numbers represented by the two linked lists into integers num1 and num2.
#3) Add the two numbers as sum = num1+num2.
#4) Convert the above-calculated sum back to a linked list using our to_linkedlist() function which will one-by-one take the digits from the end of the number passed and create a linked list using them. And finally, return it.
#ans = to_linkedlist(sum).
#4) Return the resultant linked list ‘ans’ containing the sum.
#Since our to_linkedlist() function is taking the digits from the end of the number passed to it and create a linked list by adding new nodes at the end, the resulting linked list will contain the digits of the number in reverse order.
#So, our ‘ans’ will contain the sum as a linked list containing digits of sum in reverse order.
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def addTwoLists(self, first, second):
		prev = None
		temp = None
		carry = 0

		while(first is not None or second is not None):

			fdata = 0 if first is None else first.data
			sdata = 0 if second is None else second.data
			Sum = carry + fdata + sdata

			carry = 1 if Sum >= 10 else 0

			Sum = Sum if Sum < 10 else Sum % 10

			temp = Node(Sum)

			if self.head is None:
				self.head = temp
			else:
				prev.next = temp

			prev = temp

			if first is not None:
				first = first.next
			if second is not None:
				second = second.next

		if carry > 0:
			temp.next = Node(carry)

	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end=' ')
			temp = temp.next


first = LinkedList()
second = LinkedList()

first.push(1)
first.push(5)

second.push(3)
second.push(9)
second.push(7)

res = LinkedList()
res.addTwoLists(first.head, second.head)

res.printList()
#SEE ADDITION OF 2 SINGLY LINKED LIST IMAGE TO UNDERSTAND THE PROCESS MORE CLEARLY.
