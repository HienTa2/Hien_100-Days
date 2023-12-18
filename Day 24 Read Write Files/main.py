# # open file
# file = open("test_file.txt")
#
# # read file
# content = file.read()
# print(content)
# file.close()

# with keyword will close the file with the file.close()
with open("test_file.txt") as file:
    contents = file.read()
    print(contents)

