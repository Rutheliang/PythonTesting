# no need to open/close the file using open and close codes
# optimize way -> with open ('sec7test.txt') as file:

#file = open('sec7test.txt')

with open ('sec7test.txt') as file:

    print(file.read(2))

#file.close()