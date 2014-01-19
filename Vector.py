from math import *

class Vector:
	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)

	def setR(self,x,y):
		self.x = float(y)
		self.y = float(y)

	def setP(self,r,th):
		self.x = float(float(r) * cos(th))
		self.y = float(r * sin(th))

	def dot(self,other):
		return self.x * other.x + self.y * other.y

	def cross(self,other):
		return self.x * other.y - self.y * other.x

	def coCross(self, other):
		return Vector(self.y*other, -self.x*other)

	def abs2(self):
		return self.x**2 + self.y**2

	def abs(self):
		return sqrt(self.abs2())

	def arg(self):
		return atan2(self.y, self.x)

	def __add__(self,other):
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	def __mul__(self,other):
		return Vector(other * self.x,other * self.y)

	def __div__(self,other):
		return Vector(self.x/other, self.y/other)

	def __rmul__(self,other):
		return self * other

	def __repr__(self):
		return "<" + str(self.x) + "," + str(self.y) + ">"
