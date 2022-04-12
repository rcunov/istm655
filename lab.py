import asyncio
import os
import sys
import hashlib
from random import randint
import shutil
from pathlib import Path

# remove directories and files if they exist
shutil.rmtree(Path("C:/integrity"), ignore_errors=True, onerror=None)
shutil.rmtree(Path("C:/production"), ignore_errors=True, onerror=None)

# create C:\integrity
Path("C:/integrity").mkdir()

# define function to write content into files
def writefile(file, content):
    text_file = open(file, "w")
    text_file.write(content)
    text_file.close()

# write content into files
writefile("C:/integrity/file1.txt", "File 1 is an important logging server!")
writefile("C:/integrity/file2.txt", "File 2 is an important database!")
writefile("C:/integrity/file3.txt", "File 3 is an important web server!")

# copy all files in C:\integrity to C:\production 
shutil.copytree("C:/integrity", "C:/production", dirs_exist_ok=True)

# modify one of the files in production
selection = randint(1,3)
writefile("C:/production/file" + str(selection) + ".txt", "This file has been modified! Oh no!")
print("A hacker has modified " + "C:\\production\\file" + str(selection) + ".txt!")

# define loop to hash all files in a directory with a certain algorithm
def hashdir(strdir, algo, list):
    pathdir = Path(strdir) # convert string to path
    for file in os.listdir(pathdir):
        with open(strdir + file, 'rb') as f:
            bytes = f.read() # read file as bytes
            readable_hash = algo(bytes).hexdigest() # output as text
            list.append(readable_hash) # add to list
    # print ("C:\\" + pathdir.name,str(algo().name) + ":",list) # this prints the contents of the arrays

# declare array to store C:\integrity MD5 hashes and call hashdir function
integrity_md5_list = []
hashdir("C:/integrity/", hashlib.md5, integrity_md5_list)

# declare array to store C:\production MD5 hashes and call hashdir function
prod_md5_list = []
hashdir("C:/production/", hashlib.md5, prod_md5_list)

# declare array to store C:\integrity SHA1 hashes and call hashdir function
integrity_sha1_list = []
hashdir("C:/integrity/", hashlib.sha1, integrity_sha1_list)

# declare array to store C:\production SHA1 hashes and call hashdir function
prod_sha1_list = []
hashdir("C:/production/", hashlib.sha1, prod_sha1_list)
print()

# perform hash checks. if either hash check fails, then prints error
for x in range(3):
    if (integrity_md5_list[x] != prod_md5_list[x]) | (integrity_sha1_list[x] != prod_sha1_list[x]):
        print("file" + str(x+1) + ".txt has a hash mismatch! Oh no!")
    else:
        print("file" + str(x+1) + ".txt has not been changed.")
    