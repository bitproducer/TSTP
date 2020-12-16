# recursion, a function calls itself until a condition stops it from continuing
'''
def bottles_of_beer(bob):
    if bob < 1:																												# Base case
        print("""No more bottles of beer on the wall. No more 
                 bottles of beer.""")
        return
    tmp = bob
    bob -= 1																												# change the state of the functions toward the base case
    print("""{} bottles of beer on the wall. {} bottles
             of beer. Take one down, pass it around, 
             {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)																									# as long as the base case is true, recall the function

bottles_of_beer(100)
'''

'''
def print_to_zero(n):
    if n < 0:
        return
    print(n)
    print_to_zero(n - 1)

print_to_zero(100)
'''

# binary search
def binary_search(the_list, item):
	first = 0
	last = len(the_list)-1
	found = False

	while first <= last and not found:																						# makes sure there is at least one element in the list to be searched
		mid = (first + last)//2																								# evaluates the middle of the list, the '//' returns the rounded down division result
		if the_list[mid] == item:
			found = True
		else:
			if item < the_list[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found

the_list = [10, 12, 13, 14, 15, 18, 19]
item = 10

if binary_search(the_list,item):
	print ('The item is in the list!')
else:
	print ('The item is not in the list!')
