#!/usr/bin/env python3
# Copyright 2021 Thomas Kocourek - N4FWD
import sys
import os
import re

def printHelp():
    print("lookingfor - a search tool to find a string within a directory of source files")
    print("'lookingfor help' will print this message."+'\n')
    print("Order of arguments is important"+'\n')
    print("lookingfor <source extension> <target string> <path of directory holding source code>")
    print("defaults are:  'cpp' 'def' <current directory>" + '\n')
    print("To accept a default setting, use '' as the argument.")
    quit()

# Set up defaults
fileType = "any"
searchText = "def"
whereToStart = "."
knownFileExt = ["c","cpp","cxx","h","py"]
# add any other file extensions to be checked
customFileExtension = []

# Merge the two extension lists
knownFileExt += customFileExtension

# process any CLI arguments
if len(sys.argv) == 1:
    printHelp()
if len(sys.argv) > 1:
    # Remove the name of this script
    argV = sys.argv[1:]
    askHelp = [element.upper() for element in argV]
    if len(argV) > 3:
        print("Too many arguments!\n")
        printHelp()
    if len(argV) == 1 and askHelp == ['HELP']:
        printHelp()
    index = 1
    for aArgv in argV:
        if index == 1:
            if len(aArgv) != 0:
                # use default value if none were passed (two each - single quotes = blank)
                # Otherwise assign the given extension
                fileType = aArgv
            index += 1
            continue
        if index == 2:
            if len(aArgv) != 0:
                searchText = aArgv
            index += 1
            continue
        if index == 3:
            whereToStart = aArgv
            index += 1

if fileType == "any":
    print("Looking at files with known file extensions containing the text '"+searchText+"' in directory '"+whereToStart+"'\n")
else:
    print("Looking for any file ending in '"+fileType+"' containing the text '"+searchText+"' in directory '"+whereToStart+"'\n")

tmpList = 'tmp_list.txt'
try:
    os.chdir(whereToStart)
except FileNotFoundError:
    print("Directory not found! Check spelling.")
    os.quit()
searchDir = os.getcwd()
searchFile = os.path.join(searchDir, tmpList)
listedFiles = os.listdir(searchDir)
# Get a list of source code files ending in the fileType
with open(searchFile, 'w') as s:
    for fileLines in listedFiles:
        # Lets get more specific
        # For no specified extension, loop through known extensions
        if fileType == "any":
            for ext in knownFileExt:
                searchPoint = len(fileLines) - len(ext)
                    # Parse the extension
                searchLine = fileLines[searchPoint:]
                    # Does the file extension match a known extension
                if searchLine == ext:
                        # Yes, write it out
                    s.write(fileLines +'\n')
        else:  # We have a specified extension
            searchPoint = len(fileLines) - len(fileType)
                # Parse the extension
            searchLine = fileLines[searchPoint:]
                # Check the file extension against the specified ext.
            if searchLine == fileType:
                # Yes, write it out
                s.write(fileLines +'\n')

# Open each file in the list and check if it has the desired text
# If the file has the desired text, print the name of the file
with open(searchFile,'r') as f:
    for line in f:
        fileName = os.path.join(os.getcwd(),line)
        fileName = fileName.strip()
        with open(fileName,'r') as z:
            printTarget = ""
            for theText in z:
                if re.search(searchText, theText) != None:
                    # suppress multiple listings of the same file
                    if printTarget != line:
                        print(line)
                        printTarget = line
# remove the temporary file
os.remove(searchFile)


