You are a consultant for Altius International. Your client is concerned about the integrity of the files on their server. They are concerned that a hacker would compromise these three important files. Thus, they want to run an application daily to ensure that their three key files have not been compromised.

Your job is to write a Python program that will calculate the MD5 and SHA1 hash values for three files and compare those values to the same files in another directory.

In this exercise, you will create three files (name them whatever you want) and save them in the “C:\integrity” folder. Then copy those files to the “C:\production” folder. Next, modify ones of these files in the “production” folder so that it isn’t the same as the one in the “integrity” folder. Then, write a
Python program that calculates the two hash values for each file and compares them to the hash values of the files in the other folder.

The results of this program should indicate that two of the files maintained integrity, while the other one was changed.
