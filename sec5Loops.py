
greeting = "Good Morning"

if greeting == "Morning":
    print("Condition matches")
    print("second line")
else:
    print("condition do no match")

print("if else condition code is completed")


# FOR LOOP

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)


print("****************")
for j in range(1, 6): # for (i=0; i<6; i++)
    print(j)


print("****************")
# sum of first natural numbers 1+2+3+4+5 =15
# range(i,j) -> i to j-1

summation = 0
for j in range(1, 6): # for (i=0; i<6; i++)
    summation = summation + j
print(summation)

# summation + j = summation
# 1 + 0 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15


print("****************")
# print with 2 index like 1, 1+2, 3+2,
for k in range(1, 10, 2): # for (i=0; i<5; i+2)
    print(k)

# 1 + 2 = 3
# 3 + 2 = 5
# 5 + 2 = 7
# 7 + 2 = 9


print("****************")
for m in range(6):
    print(m)


# WHILE LOOP
print("*******WHILE LOOP*********")
# it will keep on executing until it becomes false
it=4

while it>1:
    print(it)
    it = it - 1

print("*******WHILE LOOP*********")
it=4

while it>1:
    if it != 3: # remove the 3
        print(it)
    it = it - 1


print("*******WHILE LOOP*********")
it = 5

while it>1:
    if it == 3:
        break # halt the loop abruptly
    print(it)
    it = it - 1


print("*******WHILE LOOP*********")

it = 10

while it>1:
    if it == 9:
        it = it - 1
        continue # don't continue on break / go back to iteration
    if it == 3:
        break
    print(it)
    it = it - 1

print("while loop execution")
