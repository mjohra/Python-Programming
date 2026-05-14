# String
name = "Mehjabin Johra"
print(name)

# integer
age = 30
print(age)

#checking data type
print(type(age))

# floating
amount = 520.5
print(amount)
print(type(amount))

#complex
husband = 1j
print(husband)
print(type(husband))

# str type data
firstName = "Mehjabin"
lastName = "Johra"
print("Myself" +' '+firstName +' '+ lastName)

# boolean type data
x = 10
y = 5
z = x > y
print(z)
print(type(z))

# string formating
num1 = 2
num2 = 3
print(f"Total amount: {num1+num2}")

# Binary type data
myList = [1,2,3,4,5]
b = bytes(myList) # immutable-- we cant change the value
print(myList)
print(type(b))

#byteArray
myList = [1,2,3,4,5]
b1 = bytearray(myList)
print(type(b1))
print(b1[1])
b1[1]=100
print(b1[1])


