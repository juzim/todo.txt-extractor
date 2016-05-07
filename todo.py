#@todo pass filename from outside for piping
import glob
import re
from sys import argv

script, basePath = argv

types = ('php', 'js')
files_grabbed = []
for types in types:
    files_grabbed.extend(glob.glob(basePath + '/**/*.' + types, recursive=True))

foundTasks = []

for path in files_grabbed:
    with open(path) as currentFile:
        for num, line in enumerate(currentFile, 1):
            match = re.search("// ?@?(todo|TODO):? (.*)", line)
            if match:
                text = match.group(2).strip()
                shortPath = re.sub(basePath + "/", '', path)
                task = text + " @" + shortPath + ":" + str(num)
                foundTasks.append(task)

todoFile = "todo.txt"

text_file = open(todoFile, "w+")

text_file.write("\n".join(foundTasks))

text_file.close()
