#strings

#'hello' = "hello"

print('Hello')
print("Hello")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello World"
print(a[1])

#Looping through a string

for x in "banana": 
 print(x)

#length of a function
a = "Hello world!"
print(len(a))

#in

txt = "The best things in life are free!"
print("free" in txt)

#if statement

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#not

txt = "The best things in life are free!"
print("expensive" not in txt)

#ifnot

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#slicing 

b = "Hello World!"
print(b[2:5])
print(b[:5]) #slicing from the first index 
print(b[2:]) #slicing to the last index
print(b[-5:-2]) #Negative indexing 

#Uppercaase 

a = " Hello World! "
print(a.upper())

#lower case 
print(a.lower())
 
 #whitespace 
print(a.strip())

#replace
print(a.replace("H", "J"))

#split
print(a.split(","))

#string concatenation 
a = " Hello "
b = " World! "
c = a + b
print(c)

#format 

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

 
#Escape Characters txt = "We are the so-called "Vikings" from the north." #Errorxt = "We are the so-called "Vikings" from the north."

x = "Hello World"
print(len(x))