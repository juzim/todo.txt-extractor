# todo.txt-extractor
Finds and extracts all todos of a project and saves them as a [todo.txt](http://todotxt.com) file. Filename and linenumber are set as context
Currently only php and js files are supported

Usage:
python3.5 extractTasks.py FOLDERPATH

Todo:
- configurations for multiple projects
  - todo.txt file name
  - project path
  - file extensions
- argument for parsing single files (so one can pipe search results into it)
- support for more languages (find all comment variations)
- allow existing tasks in file
- update existing tasks
- remove deleted tasks/move to "done" file

Things this won't do:
- update task in source file when changed in txt
