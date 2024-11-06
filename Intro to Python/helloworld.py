age = 100
name = "Topaz"
height = 5.2
is_teacher = False
true = False
hello = "Hello World!"

#print(hello.lower())
#print(hello.upper())
#print(hello.replace("World", "Everybody"))

#print(f"Hi, my name is {name}. I'm {age ** 2} years old.")

even = 30
odd = 31

#print(f"Is this number {even} even?: {((30 % 2) == 0)}")
#print(f"Is this number {odd} even?: {((31 % 2) == 0)}")

def greet(name):
  print(f"Hello, {name}!")

greet("Topaz")

def calculate_sum(first_number, second_number):
  return first_number + second_number

print(calculate_sum(2, 3))

def explode_numbers(a, b):
  sum = calculate_sum(a, b)
  return sum ** a

print(explode_numbers(2, 5))

def go_get_donut(type):
  if(type == "maple"):
    return "I got you a maple donut"
  else:
    return "I got you a chocolate donut"
  
def check_if_greater_than_two(num):
  if(num > 2):
    print("Yeah it is")

check_if_greater_than_two(3)
print(go_get_donut("maple"))

student = {
  "name": "Topaz",
  "age": 100,
  "coach": 1
}

print(student["age"])

print(student["name"])