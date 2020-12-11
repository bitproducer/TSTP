"""
class Square:

	square_list = []

	def __init__( self, s ):
		self.width = s
		self.length = s
		self.square_list.append((self.width, self.length))


sqrt_a = Square(2)
sqrt_b = Square(6)

print (Square.square_list)
"""
"""
class Square:

	def __init__(self, side):
		self.side = side

	def calc_perimeter( self ):
		return self.side * 4

	def __print_sides__( self ):			# __ format for functions not to be touched
		return "{} by {} by {} by {}".format( self.side, self.side, self.side, self.side )

sqr = Square(213)

print (sqr.calc_perimeter())
print (sqr.__print_sides__())
"""

"""
def sameObj( obj_a, obj_b ) :
	return obj_a is obj_b

class DummyA:
	def __init__(self):
		pass

class DummyB:
	def __init__(self):
		pass

dum_a = DummyA
dum_b = DummyA

print (sameObj(dum_a,dum_b))
"""

"""
import re

zen = 'Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases arent special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless youre Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, its a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- lets do more of those!'

matches = re.findall('dutch', zen, re.IGNORECASE)				# find the word dutch in the string and ignore lower/uppercase
print (matches)
"""

"""
import re														# re stands for regular expressions, which you can use in a terminal

string = 'Arizona 479, 501, 870. California 209, 213, 650'		# create a mixed string

matches = re.findall('\d', string, re.IGNORECASE)				# find all the numbers in the string (\d = digit)
print(matches)
"""

"""
import re

string = 'The ghost that says boo haunts the loo, whooh'

matches = re.findall('.oo', string)								# find every word with a double o
print (matches)
"""

x = 100

if x<10:
	print ('x is smaller then 10')
else:
	print ('x is greater then 10')
