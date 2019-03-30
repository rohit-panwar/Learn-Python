# Storing integer value to 'a'
a = 100
print(a)

a: int = 100
print(a)

# Storing float value to 'a'
a = 100 + 23.456
print(a)

a: float = 100 + 0.001
print(a)

# Storing string value to 'a'
a = "Roh"
print(a)

a: str = "Rohit Singh Panwar"
print(a)

# Both x and y are pointint the same memory/data
x = 50
y = x
print(x, y)
print("Value Of X and Y are: ", x, y)

# Verify that both have same id or not
print(id(x))
print(id(y))

# Multiple assignment
x = y = z = 100
print(x, y, z)

x, y, z = 100, 200, 300
print(x, y, z)

# Multiplier
print((a + " :: ") * 5)

# Concatenation
print(a + " " + "is working on Python")
print(a + str(x))
