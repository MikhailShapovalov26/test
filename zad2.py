#!/usr/bin/env python3

write_file=set()
import os
dir = os.path.abspath(os.curdir)
bash_command = ["dir", "git status"]
print ('&&' .join(bash_command))
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        write_file.add(prepare_result)
print (write_file)

