#strings
str = 'Aditya'
str1 = "Hello World"
print(str,str1)

#intint1 = 0x20eger
int1 = 42  # Decimal integer
int2 = 0b101010  # Binary integer
int3 = 0o52  # Octal integer
int4 = 0x2A  # Hexadecimal integer

print(int1, int2, int3, int4)

#float
float1 = 3.14  # Decimal float
float2 = 2.5e3  # Exponential float
float3 = 1.5E-2  # Exponential float with uppercase E

print(float1, float2, float3)

#complex
complex1 = 3 + 4j  # Complex number with real and imaginary parts
complex2 = 5 - 2j  # Complex number with real and imaginary parts
complex3 = 0 + 1j  # Purely imaginary complex number


print(complex1, complex2, complex3)

#list
list1 = [1, 2, 3, 4, 5]  # List of integers
list2 = ['a', 'b', 'c']  # List of strings


print(list1, list2)

#tuple
tuple1 = (1, 2, 3)  # Tuple of integers
tuple2 = ('x', 'y', 'z')  # Tuple of strings
tuple3 = (1, 'a', 3.14)  # Tuple with mixed types

print(tuple1, tuple2, tuple3)

#dictionary
dict1 = {'name': 'Alice', 'age': 30}  # Dictionary with string keys and values
dict2 = {1: 'one', 2: 'two'}  # Dictionary with integer keys and string values

print(dict1, dict2)

#boolean
bool1 = True  # Boolean value True 
bool2 = False  # Boolean value False
bool3 = 5 > 3  # Boolean expression (True)
bool4 = 2 < 1  # Boolean expression (False)
print(bool1, bool2, bool3, bool4)

#none
none1 = None  # NoneType value representing absence of value
print(none1)

#bytes 
bytes1 = b'Hello'  # Byte string
bytes2 = bytes([65, 66, 67])  # Byte array from integer values  
bytes3 = bytes('Hello', 'utf-8')  # Byte string from regular string
print(bytes1, bytes2, bytes3)

#bytearray
bytearray1 = bytearray(b'Hello')  # Mutable byte array
bytearray2 = bytearray([65, 66, 67])  # Mutable byte array from integer values
bytearray3 = bytearray('Hello', 'utf-8')  # Mutable byte array from regular string
print(bytearray1, bytearray2, bytearray3)

#memoryview
memoryview1 = memoryview(bytes1)  # Memory view of a byte string
print(memoryview1)


#frozenset
frozenset1 = frozenset([1, 2, 3])  # Immutable set
frozenset2 = frozenset(['a', 'b', 'c'])  # Immutable set of strings

print(frozenset1, frozenset2)

#range
range1 = range(5)  # Range object from 0 to 4   
range2 = range(1, 10, 2)  # Range object from 1 to 9 with step 2
range3 = range(10, 0, -1)  # Range object from 10 to 1 in reverse order

print(list(range1), list(range2), list(range3))

#set
set1 = {1, 2, 3}  # Set of integers

print(set1)


# Creating a set with mixed types
set2 = {1, 'a', 3.14}  # Set with mixed types   
print(set2)



