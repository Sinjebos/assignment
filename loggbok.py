import time
import datetime
import os
import glob
date = datetime.datetime.now()
## creates a new file with .txt in current folder and lets the user add title, text and automaticlly adds the date it was created ##
def newFile():
    new_file = input("Create a new file or use a file that already excist\nFilename: ") + ".txt"
    file_title = input("Title for you file: ").upper()
    file_text = input("Add what you want to your file: ")
    my_file = open(new_file, 'a')
    my_file.write("\n" + file_title + "\n" + file_text + "\n" + str(date))
## removes file that user inputs if it excist ##
def removeFile():
    remove_file = input("Which file would you like to remove?\nTitle: ")
    if remove_file.endswith(".txt"):
        os.remove(remove_file)
    else:
        print("Can't remove that file")

## print all files that ends with .txt ##
def printallFiles():
    all_files = glob.glob("*.txt")
    for files in all_files:
        read_all_files = open(files, 'r')
        print(read_all_files.read())
## user search for a file that ends with .txt ##
def searchForFile():
    read_file = input("What file would you like to search for?\nFile: ") + ".txt"
    if read_file.endswith(".txt"):
        my_file = open(read_file, 'r')
        print(my_file.read())
    else:
        print("You dont have any file with that name")

## code running ##
print("Welcome to your virtual filebook")
isRunning = True
while isRunning:
    try:
        user_input = input("[1] Create a file\n[2] Search for a file that already excist\n[3] Print all saved files\n[4] Remove a saved file\n[5] Close your filebook\nOption: ")
        if user_input == "1":
            newFile()
        elif user_input == "2":
            searchForFile()
        elif user_input == "3":
            printallFiles()
        elif user_input == "4":
            removeFile()
        elif user_input == "5":
            print("Closing filebook have a nice day!")
            isRunning = False
    except Exception:
        print("Invalid input")