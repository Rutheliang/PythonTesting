file = open('sec7test.txt')

# read all the contents of file
# print(file.read()) # show all characters in test.txxt

# read n number of characters by passing parameter
# print(file.read(5)) # show "eleph"


# read one single line at a time readline()
# print(file.readline()) # first line -> show "elephantdog"
# print(file.readline()) # second line -> show "cat"


# print line by line using readline method
# line = file.readline()
# while line != "":
#    print(line)
#    line = file.readline()

# values = [abc, bvdsf, Cat, dog, elephant]
# values stored in list
for line in file.readlines():
    print(line)


file.close()