#@todo pass filename from outside for piping
import glob
import re
import os
import argparse

parser = argparse.ArgumentParser("Extract tasks from files and creates a todo.txt")

parser.add_argument('basePath', help='absolute path to project. Use "." for current directory')
parser.add_argument('-o', action="store", dest="todoFile", help='absolute path for output file')
parser.add_argument('-e', action="append", default=[], dest="types", help='File extensions')
parser.add_argument('-f', action="store", dest="specificFile", help='Parson single file only')

args = parser.parse_args()

basePath = args.basePath

if args.todoFile:
    output = args.todoFile
    if not output.endswith(".txt"):
        output += '.txt'
else:
    output = os.getcwd() + "/todo.txt"

print(output)

types = args.types

if len(types) == 0:
    types = ['php', 'js', 'py']

print(args.specificFile)

if basePath == '.':
    basePath = os.getcwd()

files_grabbed = []

if args.specificFile:
    files_grabbed.append(args.specificFile)
else:
    for types in types:
        files_grabbed.extend(glob.glob(basePath + '/**/*.' + types, recursive=True))

foundTasks = []

for path in files_grabbed:
    with open(path) as currentFile:
        for num, line in enumerate(currentFile, 1):
            match = re.search("[/#] ?@?(todo|TODO):? (.*)", line)
            if match:
                text = match.group(2).strip()
                shortPath = re.sub(basePath + "/", '', path)
                task = text + " @" + shortPath + ":" + str(num)
                foundTasks.append(task)

text_file = open(output, "w+")
text_file.write("\n".join(foundTasks))
text_file.close()

print(str(len(files_grabbed)) + " files parsed")
print(str(len(foundTasks)) + " tasks added")
