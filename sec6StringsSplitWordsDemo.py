
str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"


print(str[1]) # a

print(str[0:5])  # Rahul -> first 4 characters / if you want to substring in python

print (str+str1)  # concatenation -> RahulShettyAcademy.comConsulting firm

print(str3 in str)  #  substring check -> True

var = str.split(".")  # split the words
print(var)
print(var[0]) #  get the first one

str4 = " great " # trim
print(str4.strip())
print(str4.lstrip()) # left strip
print(str4.rstrip()) # right strip


