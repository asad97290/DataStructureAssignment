from array import *

class MyArray(object):
	def __init__(self, typecode='i', *args):
		self._typecode = typecode
		initial_values = [arg for arg in args]
		self._arr = array(typecode, initial_values)
		self._capacity = len(initial_values)
		self._size = len(args)

	# same as arr[i]; syntactic sugar
	def get(self, index):
		if index >= self._size:
			raise IndexError("invalid index")
		else:
			return self._arr[index]

	# same as arr[0] = 10; syntactic sugar
	def set(self, index, value):
		if index >= self._size:
			print("invalid index")
		else:
			self._arr[index] = value

	def size(self):
		return self._size

	def append(self, value):
		self._size += 1
		if self._size > self._capacity:
			self._arr = self.expand_capacity(self._arr)
		self._arr[self._size-1] = value
		return self


	def remove(self, value):
		index = -1
		for i in range(self._size):
			if self._arr[i] == value:
				index = i
				break;
		if index == -1:
			print("array is empty nothing to remove")
		else:	
			k = index + 1  
			while k < self._size:
				self._arr[k-1] = self._arr[k]
				k += 1
			self._size -= 1
		return self

	def insert(self, index, value):
		self._size += 1
		if index >= self._size:
			raise IndexError("Out of bound insertion.")
		elif self._size > self._capacity:
			self._arr = self.expand_capacity(self._arr)
		k = self._size
		while k > index:
			self._arr[k-1] = self._arr[k-2]
			k -= 1
		self._arr[index] = value
		return self	


	def pop(self, index = -1):
		if index >= self._size:
			raise IndexError("invalid index")
		elif self._size <= 0:
			raise IndexError("nothing to pop")
		else:
			k = index 
			while k < self._size-1:
				self._arr[k] = self._arr[k+1]
				k += 1
			self._size -= 1
		return self

	def __str__(self):
		return "arr={} size={} capacity={}".format(self._arr, self._size, self._capacity)


	def expand_capacity(self, current_arr):
		if len(current_arr) == 0:
			new_arr = array(self._typecode, [-1])
		else:
			self._capacity = 2 * len(current_arr)
			new_arr = array(self._typecode, [i for i in range(2 * len(current_arr))])
			
		for j in range(len(current_arr)):
			new_arr[j] = current_arr[j]

		return new_arr