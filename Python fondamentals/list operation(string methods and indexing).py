A = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j']

# Print the second element
print(A[1])  # Output: b

# Print the entire list
print(A) 

# Print the first five elements
print(A[0:5])  

# Print the third-to-last element
print(A[-3])  # Output: h

# Print a slice containing the third-to-last element
print(A[-3:-2])  # Output: ['h']

# Print the last and fifth-to-last elements individually
print(A[-1])  # Output: j
print(A[-5])  # Output: f
A.append('6')
print(A)
A.insert(0,'r')
print(A)
A.remove('a')
print('b' in A)
print('x' in A)
print(len(A))
x='python'
print(len(x))