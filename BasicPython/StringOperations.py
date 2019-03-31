# How to store a String in variable
str1 = "hello world! Welcome to Python 3"  # This is recommended
str2 = 'Welcome to Python, I like python for coding'  # This is also correct but not recommended

print(str1)
print(str2)

# Upper lower and capitalize
print(str1.upper())
print(str1.lower())
print(str1.capitalize())  # It is capitalize only 1st character of sentence and rest all convert to small case
print(max(str1))  # will return the biggest character
print(min(str1))  # will return the smallest character. Space 1st priority than 'a'
print(str2.replace("python", "Java"))  # Case sensitive


print(str2.count("python"))  # No of occurrences of the word
print(str2.find("python"))  # It will give index of the word

print("world" in str1)  # If word contain it will return True otherwise False. Case sensitive
print("World" in str1)
print("Java" in str1)
print("Java" not in str1)

print("My name is %s and i am %d year old" % ("Rohit", 30))

# How to write paragraph
str3 = """Hello Friends !!!
We are learning python,
and we like to write programs in python"""
print(str3)

str4 = '''Hello Friends !!!
We are learning Java,
and we like to write programs in Java'''
print(str4)

# How to print escape character
print('Why you don\'t wanna go')
print("My favorite language is \"Sanskrit\" and I can write also")

# Trimming the space from left and right
s1 = "   Rohit   "
print(s1.lstrip())
print(s1.rstrip())

# To split the string
s2 = "Runs He Walks He Eats He Sleep He Speaks"
s3 = s2.split("He")
print(s3)
print(s3[0])
print(s3[1])
print(s3[2])
print(s3[3])

s4 = "Python"
#print(s4[6])     // IndexError: string index out of range
print(s4[0]+":"+s4[1]+":"+s4[2]+":"+s4[3]+":"+s4[4]+":"+s4[5])
print(s4[-1]+":"+s4[-2]+":"+s4[-3]+":"+s4[-4]+":"+s4[-5]+":"+s4[-6])

s5 = "Python"
# To compare strings
print(s4 is s5)
print(s4 == s5)
