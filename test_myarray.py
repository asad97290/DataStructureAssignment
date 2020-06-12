 
import unittest
from MyArray import MyArray

class MyArrayTests(unittest.TestCase):

	def test_size_when_empty_myarray(self):
		# Arrange
		myarray = MyArray()
		
		# Act
		size = myarray.size()

		# Assert
		self.assertEqual(0, size)

	def test_get_when_empty_myarray(self):
		# Arrange
		myarray = MyArray()
		
		# Act & Assert
		self.assertRaises(IndexError, myarray.get, 0)

	def test_size_when_single_element_in_myarray(self):
		# Arrange
		myarray = MyArray('i', 100)
		
		# Act
		size = myarray.size()

		# Assert
		self.assertEqual(1, size)

	def test_size_when_more_than_one_element_in_myarray(self):
		# Arrange
		myarray = MyArray('i', 100, 200)
		
		# Act
		size = myarray.size()

		# Assert
		self.assertEqual(2, size)

	def test_get_when_single_element_in_myarray(self):
		# Arrange
		myarray = MyArray('i', 100)
		
		# Act
		element = myarray.get(0)

		# Assert
		self.assertEqual(100, element)

	def test_get_when_more_than_one_element_in_myarray(self):
		# Arrange
		myarray = MyArray('i', 100, 200)
		
		# Act
		element_1 = myarray.get(0)
		element_2 = myarray.get(1)

		# Assert
		self.assertEqual(100, element_1)
		self.assertEqual(200, element_2)

	def test_set_when_empty_myarray(self):
		# Arrange
		myarray = MyArray('i')

		# Act & Assert
		self.assertRaises(IndexError, myarray.set( 0, 100))

	def test_set_when_single_element_in_myarray(self):
		# Arrange
		myarray = MyArray('i', 100)

		# Act
		myarray.set(0, 200)

		# Assert
		self.assertEqual(200, myarray.get(0))

	def test_set_when_more_than_one_element_in_myarray(self):
		# Arrange
		myarray = MyArray('i', 100, 200)

		# Act
		myarray.set(1, 300)

		# Assert
		self.assertEqual(300, myarray.get(1))

	def test_append_when_empty_myarray(self):
		# Arrange
		myarray = MyArray('i')

		# Act
		myarray.append(100)

		# Assert
		self.assertEqual(1, myarray.size())
		self.assertEqual(100, myarray.get(0))

	def test_append_when_single_element_in_myarray(self):
		# Arrange
		myarray = MyArray('i', 100)

		# Act
		myarray.append(200)

		# Assert
		self.assertEqual(2, myarray.size())
		self.assertEqual(100, myarray.get(0))
		self.assertEqual(200, myarray.get(1))

	def test_append_when_more_than_one_element_in_myarray(self):
		# Arrange
		myarray = MyArray('i', 100, 200)

		# Act
		myarray.append(300)

		# Assert
		self.assertEqual(3, myarray.size())
		self.assertEqual(100, myarray.get(0))
		self.assertEqual(200, myarray.get(1))
		self.assertEqual(300, myarray.get(2))

	def test_insert_when_empty_myarray(self):
		#Arrange
		myarray = MyArray('i')

		# Act
		myarray.insert(0,100)

		# Assert
		self.assertEqual(1, myarray.size())
		self.assertEqual(100, myarray.get(0))

	def test_insert_when_myarray_is_full(self):

		myarray = MyArray('i',1,2,3,4)

		self.assertEqual(4, myarray.size())
		self.assertEqual(4, myarray._capacity)
		myarray.insert(0,0)
		self.assertEqual(5, myarray.size())
		self.assertEqual(8, myarray._capacity)

	def test_insert_is_not_full(self):

		myarray = MyArray('i',1,2,3,4)
		myarray.append(5)
		self.assertEqual(5, myarray.size())
		self.assertEqual(8, myarray._capacity)
		myarray.insert(5,6)
		self.assertEqual(6, myarray.size())
		self.assertEqual(8, myarray._capacity)
		myarray.insert(6,7)
		self.assertEqual(7, myarray.size())
		self.assertEqual(8, myarray._capacity)
		myarray.insert(7,8)
		self.assertEqual(8, myarray.size())
		self.assertEqual(8, myarray._capacity)
		myarray.insert(8,9)
		self.assertEqual(9, myarray.size())
		self.assertEqual(16, myarray._capacity)

	def test_pop_for_last_element(self):
		myarray = MyArray('i',1,2,3)
		self.assertEqual(3, myarray.size())
		self.assertEqual(3, myarray._capacity)
		myarray.pop()
		self.assertEqual(2, myarray.size())
		self.assertEqual(3, myarray._capacity)

	def test_pop_for_perticular_index(self):
		myarray = MyArray('i',1,2,3)

		myarray.pop(2)

	def test_pop_on_empty_array(self):
		myarray = MyArray('i')
		self.assertRaises(IndexError,lambda:myarray.pop(0))


	def test_pop_for_an_invalid_index(self):
		myarray = MyArray('i',1,2,3)
		self.assertRaises(IndexError,lambda:myarray.pop(3))

