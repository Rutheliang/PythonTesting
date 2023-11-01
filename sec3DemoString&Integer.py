print("hello")

# comments

a = 3
print(a)

Str = "Hello World"
print(Str)

b, c, d = 5, 6.4, "Great"

# print string and integer
# 2 braces for the 2 values - "Value is"
# separate string and integer - use .format for integer

print("{} {} {}".format("Value is", b, "number"))
# Output -> Value is 5 number
# 3 {} stands for string -> value, is, number

# Another way to print string and integer together -> Use f function -> f"Ruthel"
print(f"Value is {b} number")

# what kind of variable
print(type(b))
print(type(c))
