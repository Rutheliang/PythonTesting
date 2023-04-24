# no need to close the file using this code / optimize way -> with open ('sec7test.txt') as file:
# read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open('sec7test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)  # reverse the items present in the list
    with open('sec7test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

# check the sec7test.txt after running this code