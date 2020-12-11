"""
class Shape:																# parent class

	print ('I am a shape')

	def __init__( self ) :
		self.length = None													# need variable to run in functions
		self.width = None													# need variable to run in functions

	def print_size( self ) :
		print( """{} by {}""".format( self.width, self.length ) )

	def calculate_perimeter( self ):
		return self.width * 2 + self.length * 2

	def change_size( self, nw, nl):
		self.width += nw
		self.width += nl


class Rectangle(Shape):														# child class
	def __init__( self, w, l ):
		self.width = w
		self.length = l


class Square(Shape):
	def __init__( self, s ):
		self.width = s
		self.length = s


rec = Rectangle( 1, 2 )
sqr = Square( 2 )

print (rec.calculate_perimeter())
print(sqr.calculate_perimeter())

sqr.change_size(2,3)
print(sqr.calculate_perimeter())
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
