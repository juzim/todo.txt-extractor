# todo.txt-extractor
Finds and extracts all todos of a project and saves them as a [todo.txt](http://todotxt.com) file. Filename and linenumber are set as context.
Currently all files that use "//" or "#" for comments are supported (I think), task have to start with todo/TODO/@todo/@TODO


Usage:
python3 extractTasks.py FOLDERPATH

Aruguments:
-o output file name
-e (multiple) set file extensions, defaults to php, js and py
-f parse single file
-h show help

Example:
python3 extractTasks.py /home/thisisme/dev/kittendeathmatch.com -e php -e js -o kittenstodo.txt

Todo:
- support for configurations files instead of arguments
- support for more languages (find all comment variations)
- allow existing tasks in file
- update existing tasks
- remove deleted tasks/move to "done" file
- don't overwrite existing files
- add examples for using folder watchers to pass in changed files
- tests
- clean up


Things this won't do:
- update task in source file when changed in txt
