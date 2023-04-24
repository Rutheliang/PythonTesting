values = [1, 2, "ruthel", 4, 5]
# List is data type that allows multiple values and can be different data types
print(values[0])  # 1

print(values[3])  # 4


print(values[-1])  # refer to last index of the list

print(values[1:3])  # 2 ruthel

values.insert(3, "villaespin")  # [1, 2, 'ruthel', 'villaespin', 4, 5]
print(values)

values.append("End")  # [1, 2, 'ruthel', 'villaespin', 4, 5, 'End']
print(values)

values[2] = "RUTHEL"  # Updating
del values[0]  # [2, 'RUTHEL', 'villaespin', 4, 5, 'End']
print(values)

# Tuple - Same as LIST Data type but immutable meaning you cannot change the existing behavior / use square bracket []
# LIST - mutable like updating the name ruthel to all capital letters / use parenthesis ()

val = (1, 2, "ruth", 4.5)

print(val[1])

# val[2] = "RUTH" -> error since you can't update value in tuple


#  DICTIONARY - in flower bracket / it has a key value pair
dic = {"a": 2, 4: "bcs", "c": "Hello World"}
print(dic[4])
print(dic["c"])


#
dict = {} # load/addd value in empty dictionary

dict["firstname"] = "Ruth"

dict["lastname"] = "Villa"

dict["gender"] = "Female"

print(dict)
print(dict["lastname"])






