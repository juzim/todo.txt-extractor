# todo.txt-extractor
Finds and extracts all todos of a project and saves them as a [todo.txt](http://todotxt.com) file. Filename and linenumber are set as context
Currently only php and js files are supported

Usage:
python3 extractTasks.py FOLDERPATH

Aruguments:
-o output file name
-e (multiple) set file extensions, defaultsa to php, js and py
-f parse single file

Example:
python3 extractTasks.py /home/thisisme/dev/kittensdeathmatch.com -e php -e js -o kittenstodo.txt

Todo:
- configurations for multiple projects
  - todo.txt file name
  - project path
  - file extensions
  - exclude folders
- support for more languages (find all comment variations)
- allow existing tasks in file
- update existing tasks
- remove deleted tasks/move to "done" file
- don't overwrite existing files
- add tutorials for using folder watchers to pass in changed files

Things this won't do:
- update task in source file when changed in txt
