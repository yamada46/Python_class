#! /Users/gailyamada/PycharmProjects/ITFDN2018/venv/bin/python3
'''
Mod6_Lab2
From your terminal, perform the following tasks:

Create a new directory called testing
Change into the new directory
Create a new file called test.txt
List the contents of the directory to make sure that your file was created
Add a line to the file that says "line1"
Add a line to the file that says "line2"
Add another a total of ten lines, as above (line3,line4,etc.)
View the first three lines of the file
View the last five lines of the file
Stretch Goal: can you figure out how to count the number of lines in the file using the "wc" command?

Unix:
cd /Users/gailyamada/PycharmProjects/ITFDN2018
$ mkdir testing
$ cd testing
$ touch test.txt
$ ls
test.txt
$ echo "line1" > test.txt
$ echo "line2" >> test.txt
$ cat test.txt
line1
line2
$ echo "line3" >> test.txt
$ echo "line4" >> test.txt
$ echo "line5" >> test.txt
$ echo "line6" >> test.txt
$ echo "line7" >> test.txt
$ echo "line8" >> test.txt
$ echo "line9" >> test.txt
$ echo "line10" >> test.txt
$ head -3 test.txt
line1
line2
line3
$ tail -5 test.txt
line6
line7
line8
line9
line10
$ wc test.txt
      10      10      61 test.txt
$ cat test.txt |wc
      10      10      61
# why does it print that for 'wc'

'''
'''
Python:
Change to your documents directory (My Documents on windows)
Count the number of Word and pdf files in your documents folder
Count the number of subdirectories in your documents folder
'''
import os
# change to Documents folder
os.chdir("/Users/gailyamada/Documents")

# list the current working directory
os.getcwd()
#'/Users/gailyamada/Documents'

# list what is in the directory
os.listdir()
#['.localized', 'test.txt']


# Count number of files (.txt or .doc or .pdf in documents folder
# why doesn't this work?
num_files = []
for file in os.listdir():
    if file.endswith(".txt") or file.endswith(".pdf"):
        num_files.append(file)
    else:
        print("No word or pdf files found.")

print(num_files)

# count number of subdirectories in documents folder
directories = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        directories.append(os.path.join(root, name))

print(directories)
print("There are " + str(len(directories)) + " subdirectories in the documents folder.")
