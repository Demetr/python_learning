## Uncomment these if working locally, else let the following code cell run.

# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example1.txt'
# urllib.request.urlretrieve(url, filename)
#
# ## Download Example file
# !wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt
#
# from pyodide.http import pyfetch
#
# import pandas as pd
#
# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"
#
# async def download(url, filename):
#
#     response = await pyfetch(url)
#
#     if response.status == 200:
#
#         with open(filename, "wb") as f:
#
#             f.write(await response.bytes())
#
# await download(filename, "example1.txt")
# print("done")

# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")


# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode


# Read the file
FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line
print(FileContent)

# Type of file content
type(FileContent)

# Close file after finish
file1.close()

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
file1.closed


# See the content of file
print(FileContent)


# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))


# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))


# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))


# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())


with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1


# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()


# Print the first line
FileasList[0]


# Print the third line
FileasList[2]



# Write line to file
exmp2 = '/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
# We can read the file to see if it worked:

# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
# We can write multiple lines:

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
# The method .write() works similar to the method .readline(), except instead of reading a new line it writes a new line. The process is illustrated in the figure. The different colour coding of the grid represents a new line added to the file after each method call.

# Image
# You can check the file to see if your results are correct

# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
# We write a list to a .txt file as follows:

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
# Write the strings in the list to text file
with open('/Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
# We can verify the file is written by reading it and printing out the values:

# Verify if writing to file is successfully executed
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
# However, note that setting the mode to w overwrites all the existing data in the file.

with open('/Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
# Appending Files
# We can write to files without losing any of the existing data as follows by setting the mode argument to append: a. you can append a new line as follows:

# Write a new line to text file
with open('/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
# You can verify the file has changed by running the following cell:

# Verify if the new line is in the text file
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# Additional modes
with open('/Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())


with open('/Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing')
    else:
            print(testwritefile.read())

    testwritefile.seek(0,0) # move 0 bytes from beginning.

    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
            print('Read nothing')
    else:
            print(data)

    print("Location after read: {}".format(testwritefile.tell()) )



with open('/Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file

    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())


# Copy file to another

with open('/Example2.txt','r') as readfile:
    with open('/Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


# Verify if the copy is successfully executed

with open('/Example3.txt','r') as testwritefile:
    print(testwritefile.read())


#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)



'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
        #TODO: Open the exMem file in a+ mode

        #TODO: Read each member in the currentMem (1 member per row) file into a list.
        # Hint: Recall that the first line in the file is the header.

        #TODO: iterate through the members and create a new list of the innactive members

        # Go to the beginning of the currentMem file
        # TODO: Iterate through the members list.
        # If a member is inactive, add them to exMem, otherwise write them into currentMem



    pass # Remove this line when done implementation


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())


def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = "testWrite.txt"
testAppend = "testAppend.txt"
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()

# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False

for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))


