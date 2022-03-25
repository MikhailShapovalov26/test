#!/usr/bin/env python3
import sys
write_file=set()
import os
filename =  input ('Вв :')

print (filename)

if filename == '':
	dir = os.path.abspath(os.curdir)
	print (dir)
	bash_command = ["cd "+dir, "git status"]
else:
	dir = os.path.abspath(filename)
	print ('2' + dir)
	bash_command = ["cd "+dir, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        write_file.add(prepare_result)
print (write_file)

